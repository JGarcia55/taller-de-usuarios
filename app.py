from flask import Flask
from dotenv import load_dotenv
from db import db, init_db
from models.user import User
from controllers.user_controller import user_blueprint
import os

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
#init_db(app)

@app.route('/')
def index():
    return "Hello world!"
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(debug=True)