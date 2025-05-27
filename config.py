import os
class Config:
    BASE_UPLOAD_FOLDER = os.getenv('BASE_UPLOAD_FOLDER', 'static/images')
    CAR_UPLOAD_FOLDER = os.path.join(BASE_UPLOAD_FOLDER, 'cars')
    CAB_UPLOAD_FOLDER = os.path.join(BASE_UPLOAD_FOLDER, 'cabs')
    BUS_UPLOAD_FOLDER = os.path.join('static', 'images', 'buses')

    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(24))
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///cars.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def is_allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS
