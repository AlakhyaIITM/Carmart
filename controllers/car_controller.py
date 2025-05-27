from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from datetime import datetime
import os
from models.car_model import Car, db
from models.cab_model import Cab
from models.bus_model import Bus
from controllers.utils import allowed_file

car_bp = Blueprint('car_bp', __name__)

@car_bp.app_template_filter('inr')
def format_inr(value):
    try:
        value = int(value)
        return f"₹{value:,}"
    except ValueError:
        return f"₹{value}"

@car_bp.route('/')
def index():
    page = int(request.args.get("page", 1))
    per_page = 5
    sort_by = request.args.get("sort_by", "price")
    reverse = sort_by == "price"

    cars_query = Car.query.order_by(Car.price.desc() if reverse else Car.price.asc())
    car_paginated = cars_query.paginate(page=page, per_page=per_page)
    cabs = Cab.query.order_by(Cab.year.desc()).all()
    buses = Bus.query.all()

    return render_template(
        'index.html',
        cars=car_paginated.items,
        cabs=cabs,
        buses=buses,
        page=car_paginated.page,
        total_pages=car_paginated.pages,
        sort_by=sort_by
    )

@car_bp.route('/caradd', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        try:
            car = Car(
                make=request.form['make'],
                model=request.form['model'],
                year=request.form['year'],
                price=request.form['price'],
                description=request.form.get('description', ''),
                kilometers_driven=request.form.get('kilometers_driven', 'N/A'),
                fuel_type=request.form.get('fuel_type', 'N/A'),
                transmission=request.form.get('transmission', 'N/A'),
                color=request.form.get('color', 'N/A'),
                owner_number=request.form.get('owner_number', 'N/A'),
                manufacturing_year=request.form.get('manufacturing_year', 'N/A'),
                registration_year=request.form.get('registration_year', 'N/A'),
                registration_type=request.form.get('registration_type', 'N/A'),
                location=request.form.get('location', 'N/A'),
                seller_name=request.form.get('seller_name', ''),
                seller_contact=request.form.get('seller_contact', ''),
                last_updated=datetime.now().strftime('%d %b %Y, %I:%M %p')
            )

            car.set_specifications({
                'Engine Displacement': request.form.get('engine', 'N/A'),
                'Mileage': request.form.get('mileage', 'N/A'),
                'Fuel Tank Capacity': request.form.get('fuel_tank', 'N/A'),
                'Seating Capacity': request.form.get('seating_capacity', ''),
                'Body Type': request.form.get('body_type', '')
            })

            car.set_features([f.strip() for f in request.form.get('features', '').split(',') if f.strip()])

            images = request.files.getlist("images")
            image_filenames = []
            for image in images:
                if image and allowed_file(image.filename):
                    filename = f"{car.make}_{car.model}_{datetime.now().timestamp()}_{secure_filename(image.filename)}"
                    image.save(os.path.join('static/images/cars', filename))
                    image_filenames.append(filename)
            car.set_images(image_filenames or ['default-car.png'])

            db.session.add(car)
            db.session.commit()
            flash("Car added successfully!", "success")
            return redirect(url_for('car_bp.index'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error adding car: {str(e)}", "danger")
            return redirect(url_for('car_bp.add_car'))
    return render_template('add_car.html')

@car_bp.route('/car/<int:car_id>')
def view_car(car_id):
    car = Car.query.get_or_404(car_id)
    specifications = car.get_specifications()
    features = car.get_features()
    return render_template('view_car.html', car=car, specifications=specifications, features=features)

@car_bp.route('/caredit')
def list_cars_for_edit():
    cars = Car.query.order_by(Car.last_updated.desc()).all()
    return render_template('list_cars_edit.html', cars=cars)

@car_bp.route('/edit/<int:car_id>', methods=['GET', 'POST'], endpoint='edit_car')
def edit_car(car_id):
    car = Car.query.get_or_404(car_id)
    if request.method == 'POST':
        try:
            car.make = request.form['make']
            car.model = request.form['model']
            car.year = request.form['year']
            car.price = request.form['price']
            car.description = request.form.get('description', '')
            car.kilometers_driven = request.form.get('kilometers_driven', 'N/A')
            car.fuel_type = request.form.get('fuel_type', 'N/A')
            car.transmission = request.form.get('transmission', 'N/A')
            car.color = request.form.get('color', 'N/A')
            car.owner_number = request.form.get('owner_number', 'N/A')
            car.manufacturing_year = request.form.get('manufacturing_year', 'N/A')
            car.registration_year = request.form.get('registration_year', 'N/A')
            car.registration_type = request.form.get('registration_type', 'N/A')
            car.location = request.form.get('location', 'N/A')
            car.seller_name = request.form.get('seller_name', '')
            car.seller_contact = request.form.get('seller_contact', '')
            car.last_updated = datetime.now().strftime('%d %b %Y, %I:%M %p')

            car.set_specifications({
                'Engine Displacement': request.form.get('engine', 'N/A'),
                'Mileage': request.form.get('mileage', 'N/A'),
                'Fuel Tank Capacity': request.form.get('fuel_tank', 'N/A'),
                'Seating Capacity': request.form.get('seating_capacity', ''),
                'Body Type': request.form.get('body_type', '')
            })

            car.set_features([f.strip() for f in request.form.get('features', '').split(',') if f.strip()])

            db.session.commit()
            flash("Car updated successfully!", "success")
            return redirect(url_for('car_bp.list_cars_for_edit'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error updating car: {str(e)}", "danger")
    return render_template('edit_car.html', car=car)

@car_bp.route('/delete/<int:car_id>', methods=['POST'])
def delete_car(car_id):
    try:
        car = Car.query.get_or_404(car_id)
        db.session.delete(car)
        db.session.commit()
        flash("Car deleted successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting car: {str(e)}", "danger")
    return redirect(url_for('car_bp.index'))
