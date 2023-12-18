"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake, DEFAULT_IMAGE

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)


@app.route('/api/cupcakes')
def get_cupcakes_data():
    cupcakes = Cupcake.query.all()
    
    return jsonify(cupcakes = [c.serialize() for c in cupcakes])

@app.route('/api/cupcakes/<int:id>')
def get_cupcake_data(id):
    cupcake = Cupcake.query.get_or_404(id)
    
    return jsonify(cupcake = cupcake.serialize())

@app.route('/api/cupcakes', methods = ["POST"])
def create_cupcake():
    data = request.json
    flavor = data.get("flavor")
    size = data.get("size")
    rating = data.get("rating")
    image = data.get("image", DEFAULT_IMAGE) 
    cupcake = Cupcake(flavor = flavor, size = size, rating = rating, image = image)

    db.session.add(cupcake)
    db.session.commit()
    return (jsonify(cupcake=cupcake.serialize()), 201)


@app.route('/api/cupcakes/<int:id>', methods = ["PATCH"])
def edit_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    data = request.json

    cupcake.flavor = data.get("flavor", cupcake.flavor)
    cupcake.size = data.get("size", cupcake.size)
    cupcake.rating = data.get("rating", cupcake.rating)
    cupcake.image = data.get("image", cupcake.image)
    db.session.commit()
    return jsonify(cupcake = cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods = ["DELETE"])
def del_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify({'message': 'deleted'})

@app.route('/') 
def home():
    return render_template('index.html')