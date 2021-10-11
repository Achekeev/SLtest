from flask import Flask
from flask_restful import Api

UPLOAD_FOLDER = "./static/files/"

app = Flask(__name__)
api = Api(app)
app.secret_key = "secret key"
app.config["UPLOAD_FOLDER"] = "./static/files/"
