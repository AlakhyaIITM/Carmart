from flask import Flask, send_from_directory
from config import Config
from controllers.car_controller import car_bp
from controllers.cab_controller import cab_bp
from controllers.bus_controller import bus_bp 
from controllers.admin_controller import admin_bp
import os
from extensions import db, migrate

# ✅ Import models so Flask-Migrate can detect them
from models.car_model import Car
from models.cab_model import Cab
from models.bus_model import Bus 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(car_bp)
    app.register_blueprint(cab_bp)
    app.register_blueprint(bus_bp) 
    app.register_blueprint(admin_bp)

    os.makedirs(app.config.get('UPLOAD_FOLDER', 'uploads'), exist_ok=True)
    os.makedirs(app.config.get('CAB_UPLOAD_FOLDER', 'uploads/cabs'), exist_ok=True)

    @app.route('/uploads/<path:filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    @app.route('/uploads/cabs/<path:filename>')
    def uploaded_cab_file(filename):
        return send_from_directory(app.config['CAB_UPLOAD_FOLDER'], filename)

    return app
    
app = create_app()

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

