import os
from flask import Blueprint, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
from extensions import db
from models.bus_model import Bus

bus_bp = Blueprint('bus', __name__)
BUS_UPLOAD_FOLDER = os.path.join('static', 'images', 'buses')

# Route: Add new bus
@bus_bp.route('/busadd', methods=['GET', 'POST'])
def add_bus():
    if request.method == 'POST':
        name = request.form['name']
        model = request.form['model']
        seating_capacity = request.form['seating_capacity']
        image = request.files['image']

        filename = None
        if image:
            filename = secure_filename(image.filename)
            image.save(os.path.join(BUS_UPLOAD_FOLDER, filename))

        new_bus = Bus(
            name=name,
            model=model,
            seating_capacity=seating_capacity,
            image_filename=filename
        )
        db.session.add(new_bus)
        db.session.commit()
        flash("Bus added successfully!", "success")
        return redirect(url_for('bus.list_buses'))

    return render_template('add_bus.html')

# Route: List all buses for editing/deleting
@bus_bp.route('/busedit')
def list_buses():
    buses = Bus.query.all()
    return render_template('edit_bus.html', buses=buses)

# Route: Edit a specific bus
@bus_bp.route('/editbus/<int:bus_id>', methods=['GET', 'POST'])
def edit_bus(bus_id):
    bus = Bus.query.get_or_404(bus_id)

    if request.method == 'POST':
        bus.name = request.form['name']
        bus.model = request.form['model']
        bus.seating_capacity = request.form['seating_capacity']

        image = request.files.get('image')
        if image and image.filename:
            filename = secure_filename(image.filename)
            image.save(os.path.join(BUS_UPLOAD_FOLDER, filename))
            bus.image_filename = filename

        db.session.commit()
        flash("Bus updated successfully!", "success")
        return redirect(url_for('bus.list_buses'))

    return render_template('edit_single_bus.html', bus=bus)

# Route: Delete a specific bus
@bus_bp.route('/deletebus/<int:bus_id>', methods=['POST'])
def delete_bus(bus_id):
    bus = Bus.query.get_or_404(bus_id)

    if bus.image_filename:
        image_path = os.path.join(BUS_UPLOAD_FOLDER, bus.image_filename)
        if os.path.exists(image_path):
            os.remove(image_path)

    db.session.delete(bus)
    db.session.commit()
    flash("Bus deleted successfully!", "success")
    return redirect(url_for('bus.list_buses'))
