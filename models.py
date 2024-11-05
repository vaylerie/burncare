from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/burncare?ssl_disabled=1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    nama = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    token = db.Column(db.String(128), nullable=True)
    uploads = db.relationship('UploadIdentifikasi', backref='user', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class UploadIdentifikasi(db.Model):
    __tablename__ = 'upload_identifikasi'
    id = db.Column(db.Integer(), primary_key=True)
    file_path = db.Column(db.String(255), nullable=False)
    waktu_upload = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=True)
    results = db.relationship('HasilUpload', backref='upload_identifikasi', lazy=True)

class HasilUpload(db.Model):
    __tablename__ = 'hasil_upload'
    id = db.Column(db.Integer(), primary_key=True)
    derajat_klasifikasi = db.Column(db.Integer(), nullable=False)
    confidence_score = db.Column(db.Float, nullable=False)
    deskripsi = db.Column(db.String(255), nullable=False)
    upload_identifikasi_id = db.Column(db.Integer(), db.ForeignKey('upload_identifikasi.id'), nullable=True)
    histories = db.relationship('RiwayatIdentifikasi', backref='hasil_upload', lazy=True)

class RiwayatIdentifikasi(db.Model):
    __tablename__ = 'riwayat_identifikasi'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=True)
    hasil_upload_id = db.Column(db.Integer(), db.ForeignKey('hasil_upload.id'), nullable=True)