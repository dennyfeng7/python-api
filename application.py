from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"Name: {self.name} -  Description: {self.description}"


@app.route('/')
def index():
    return "Testing connection, hello!"

# Query all 
@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()

    output = []

    for drink in drinks:
        drink_data = {"name": drink.name, "description": drink.description}

        output.append(drink_data)
    return {"drink" : output}

# Query specific 
@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name, "description": drink.description}

# Query ADD
@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}

# Query DELETE
@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"Error": "Not found"}
    db.session.delete(drink) 
    db.session.commit()
    return {"Message": "Sucessfully deleted."}
    
if __name__ == "__main__":
    app.run()