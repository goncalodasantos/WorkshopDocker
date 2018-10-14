from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@postgres/example"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def hello():
    return "Hello, World!"


@app.route('/stuff')
def stuff():
    data = User.query.all()
    result = [str(d.__dict__) for d in data]
    return json.dumps(result)





if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')