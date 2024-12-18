from flask import Flask, request, jsonify
from flask_restful import Resource
from models import User, db, UploadIdentifikasi, HasilUpload, RiwayatIdentifikasi
from keras.models import load_model
from PIL import Image
import numpy as np
import os
import logging

app = Flask(__name__)

model = load_model('model.h5', compile=False)
labels = [1, 2, 3]

def preprocess(image, target_size=(224, 224)):
    image = image.resize(target_size)
    image_array = np.array(image) / 255.
    return image_array

def prediction(file_path):
    im = Image.open(file_path)
    input_size = (224, 224)
    X = preprocess(im, input_size)
    X = np.reshape(X, (1, *X.shape))  
    y = model.predict(X)
    confidence_score = np.max(y)  
    class_index = np.argmax(y)  
    derajat_klasifikasi = labels[class_index]
    return confidence_score, derajat_klasifikasi

class ClassifyResource(Resource):
    @app.route('/api/upload', methods=['POST'])
    def post(self):
        token = request.headers.get("X-API-TOKEN")
        if not token:
            return {"data": "Unauthorized"}, 401
        user = User.query.filter_by(token=token).first()
        user_id = user.id

        if 'image' not in request.files:
            return {"data": "Failed to upload image"}, 400

        file = request.files['image']
        if file.filename == '':
            return {"data": "Failed to upload image"}, 400

        try:
            file_path = os.path.join('static/img/predict_img/', file.filename)
            file.save(file_path)

            upload_record = UploadIdentifikasi(file_path=file_path,
                                               user_id=user_id)
            db.session.add(upload_record)
            db.session.commit()

            upload_identifikasi_id = upload_record.id
            confidence_score, derajat_klasifikasi = prediction(file_path)

            hasil_record = HasilUpload(derajat_klasifikasi=derajat_klasifikasi, 
                                       confidence_score=confidence_score,
                                       upload_identifikasi_id=upload_identifikasi_id)
            db.session.add(hasil_record)
            db.session.commit()

            history_record = RiwayatIdentifikasi(user_id=user_id,
                                                 hasil_upload_id=hasil_record.id)
            db.session.add(history_record)
            db.session.commit()

            return {"data": 
                    {"derajat_klasifikasi": derajat_klasifikasi,
                    "confidence_score": str(confidence_score),
                    "deskripsi": "Image classified successfully."
                    }
            }, 200

        except Exception as e:
            logging.error(f"Error occurred: {e}")
            return {"data": "Failed to upload image"}, 500