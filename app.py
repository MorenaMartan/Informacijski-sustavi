from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SalonSync_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Usluga(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    

    def __init__(self, name, price):
        self.name = name
        self.price = price
       
@app.route('/')
def home():
    db.create_all()
    return render_template('home.html')

# CRUD operations for usluge
@app.route('/usluge')
def usluge():
    
    sort_by = request.args.get('sort_by', 'name')  # Default sort by name
    if sort_by not in ['name', 'price']:
        sort_by = 'name'
    
    all_usluge = Usluga.query.order_by(getattr(Usluga, sort_by)).all()
    return render_template('services.html', usluge=all_usluge)

@app.route('/usluge/new', methods=['GET', 'POST'])
def new_usluga():
    if request.method == 'POST':
        usluga = Usluga(
            request.form['name'],
            request.form['price']
           
        )
        db.session.add(usluga)
        db.session.commit()
        flash('New usluga added successfully.')
        return redirect(url_for('usluge'))
    return render_template('new_service.html')

@app.route('/usluge/edit/<int:usluga_id>', methods=['GET', 'POST'])
def edit_usluga(usluga_id):
    usluga = Usluga.query.get_or_404(usluga_id)
    if request.method == 'POST':
        usluga.name = request.form['name']
        usluga.price = request.form['price']
        db.session.commit()
        flash('Usluga updated successfully.')
        return redirect(url_for('usluge'))
    return render_template('edit_service.html', usluga=usluga)

@app.route('/usluga/delete/<int:usluga_id>', methods=['POST'])
def delete_usluga(usluga_id):
    usluga = Usluga.query.get_or_404(usluga_id)
    db.session.delete(usluga)
    db.session.commit()
    flash('Usluga deleted successfully.')
    return redirect(url_for('usluga'))

if __name__ == "__main__":
    app.run(debug=True)
