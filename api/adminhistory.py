from flask import Flask, request
from flask_restful import Resource
from models import db, User, RiwayatIdentifikasi, HasilUpload, UploadIdentifikasi

app = Flask(__name__)

class AdminHistory(Resource):
    @app.route('/api/admin/history', methods=['GET'])
    def get(self):
        token = request.headers.get("X-API-TOKEN")
        if not token:
            return {"data": "Unauthorized"}, 401
        
        users = User.query.filter_by(role='General').all()
        history_data = []

        for user in users:
            history_record = RiwayatIdentifikasi.query.filter_by(user_id=user.id).all()
            if not history_record:
                continue                
        
            for record in history_record:
                hasil_upload = HasilUpload.query.filter_by(id=record.hasil_upload_id).first()
                upload_identifikasi = UploadIdentifikasi.query.filter_by(id=hasil_upload.upload_identifikasi_id).first()
                if hasil_upload and upload_identifikasi:
                    history_data.append({
                        "username": user.username,
                        "waktu_upload": str(upload_identifikasi.waktu_upload),
                        "file_path": upload_identifikasi.file_path,
                        "derajat_klasifikasi": hasil_upload.derajat_klasifikasi,
                        "confidence_score": hasil_upload.confidence_score,
                        "deskripsi": hasil_upload.deskripsi
                    })
        if not history_data:
            return {"data": "No history found"}, 404
        
        return ({"data": history_data}), 200