from flask import Flask, request, jsonify
from flask_restful import Resource
from models import User, db, RiwayatIdentifikasi, HasilUpload, UploadIdentifikasi
import logging

app = Flask(__name__)

class HistoryResource(Resource):
    @app.route('/api/history', methods=['GET'])
    def get(self):
        token = request.headers.get("X-API-TOKEN")
        if not token:
            return {"data": "Unauthorized"}, 401
        
        user = User.query.filter_by(token=token).first()

        history_record = RiwayatIdentifikasi.query.filter_by(user_id=user.id).all()
        if not history_record:
            return {"data": "No history found"}, 404
        
        history_data = []

        for record in history_record:
            hasil_upload = HasilUpload.query.filter_by(id=record.hasil_upload_id).first()
            upload_identifikasi = UploadIdentifikasi.query.filter_by(id=hasil_upload.upload_identifikasi_id).first()

            if hasil_upload and upload_identifikasi:
                history_data.append({
                    "waktu_upload": str(upload_identifikasi.waktu_upload),
                    "file_path": upload_identifikasi.file_path,
                    "derajat_klasifikasi": hasil_upload.derajat_klasifikasi,
                    "confidence_score": hasil_upload.confidence_score,
                    "deskripsi": hasil_upload.deskripsi
                })

        return ({"data": history_data}), 200
