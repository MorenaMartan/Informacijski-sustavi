from flask import Flask, render_template, redirect, url_for, request, flash
from forms import ServiceForm
from database import db
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from models import Service

@app.route('/')
def index():
    services = Service.query.all()
    return render_template('index.html', services=services)

@app.route('/service/new', methods=['GET', 'POST'])
def new_service():
    form = ServiceForm()
    if form.validate_on_submit():
        new_service = Service(name=form.name.data, description=form.description.data, price=form.price.data)
        db.session.add(new_service)
        db.session.commit()
        flash('Service created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('new_service.html', form=form)

@app.route('/service/edit/<int:service_id>', methods=['GET', 'POST'])
def edit_service(service_id):
    service = Service.query.get_or_404(service_id)
    form = ServiceForm(obj=service)
    if form.validate_on_submit():
        service.name = form.name.data
        service.description = form.description.data
        service.price = form.price.data
        db.session.commit()
        flash('Service updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('edit_service.html', form=form)

@app.route('/service/delete/<int:service_id>', methods=['POST'])
def delete_service(service_id):
    service = Service.query.get_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    flash('Service deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
