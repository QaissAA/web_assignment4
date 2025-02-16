from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'db': 'task_manager', 'host': os.getenv('MONGO_URI')}
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET')

db = MongoEngine(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
