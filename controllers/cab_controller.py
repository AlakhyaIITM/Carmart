from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from datetime import datetime
import os

from models.cab_model import Cab, CabImage, db
from controllers.utils import allowed_file

cab_bp = Blueprint('cab_bp', __name__)

# Route: View all cabs (for /cab page)
@cab_bp.route('/cab')
def view_cabs():
    cabs = Cab.query.order_by(Cab.id.desc()).all()
    return render_template('view_cabs.html', cabs=cabs)

# Route: Add a new cab
@cab_bp.route('/admin/cabadd', methods=['GET', 'POST'])
def add_cab():
    if request.method == 'POST':
        try:
            new_cab = Cab(
                make=request.form['make'],
                model=request.form['model'],
                year=request.form['year'],
                seating_capacity=request.form['seating_capacity'],
                ac='ac' in request.form
            )
            db.session.add(new_cab)
            db.session.commit()

            images = request.files.getlist("images")
            for image in images:
                if image and allowed_file(image.filename):
                    filename = f"{new_cab.make}_{new_cab.model}_{datetime.now().timestamp()}_{secure_filename(image.filename)}"
                    image_path = os.path.join('static/images/cabs', filename)
                    image.save(image_path)

                    cab_image = CabImage(filename=filename, cab_id=new_cab.id)
                    db.session.add(cab_image)

            db.session.commit()
            flash("Cab added successfully!", "success")
            return redirect(url_for('cab_bp.add_cab'))

        except Exception as e:
            db.session.rollback()
            flash(f"Error adding cab: {str(e)}", "danger")

    return render_template('add_cab.html')

# Route: View single cab details
@cab_bp.route('/cab/<int:cab_id>')
def view_cab(cab_id):
    cab = Cab.query.get_or_404(cab_id)
    return render_template('view_cab.html', cab=cab)

# Route: List cabs for editing
@cab_bp.route('/admin/cabedit')
def list_cabs_for_edit():
    cabs = Cab.query.order_by(Cab.year.desc()).all()
    return render_template('list_cabs_edit.html', cabs=cabs)

# Route: Edit a cab
@cab_bp.route('/admin/cab/edit/<int:cab_id>', methods=['GET', 'POST'])
def edit_cab(cab_id):
    cab = Cab.query.get_or_404(cab_id)

    if request.method == 'POST':
        try:
            cab.make = request.form['make']
            cab.model = request.form['model']
            cab.year = request.form['year']
            cab.seating_capacity = request.form['seating_capacity']
            cab.ac = 'ac' in request.form
            db.session.commit()

            flash("Cab updated successfully!", "success")
            return redirect(url_for('cab_bp.list_cabs_for_edit'))

        except Exception as e:
            db.session.rollback()
            flash(f"Error updating cab: {str(e)}", "danger")

    return render_template('edit_cab.html', cab=cab)

# Route: Delete a cab
@cab_bp.route('/admin/cab/delete/<int:cab_id>', methods=['POST'])
def delete_cab(cab_id):
    try:
        cab = Cab.query.get_or_404(cab_id)

        for image in cab.images:
            image_path = os.path.join('static/images/cabs', image.filename)
            if os.path.exists(image_path):
                os.remove(image_path)
            db.session.delete(image)

        db.session.delete(cab)
        db.session.commit()
        flash("Cab deleted successfully!", "success")

    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting cab: {str(e)}", "danger")

    return redirect(url_for('cab_bp.view_cabs'))
