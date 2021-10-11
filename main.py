from flask import jsonify
from werkzeug.utils import secure_filename
import json
import os
from flask import request
from app import app
from database.mongo import db
from bson import json_util, ObjectId


@app.route("/file-upload", methods=["POST"])
async def upload_file():
    json_file = request.files["file"]
    if json_file.filename.endswith(".json"):
        filename = secure_filename(json_file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        json_file.save(file_path)
        resp = jsonify({"message": "File successfully uploaded"})
        resp.status_code = 201
        with open(file_path, "r") as json_data:
            text = json_data.read()
            db.collection.insert_one(json.loads(text))
            last = db.collection.find().sort("_id", -1).limit(1)[0]["_id"]
            return json.loads(json_util.dumps(last))
    else:
        return {"message": "Wrong file extension, Please upload only json files"}


app.add_url_rule("/", endpoint="/")


@app.endpoint("/")
async def get_by_id():
    object_id = request.form["object_id"]
    data = db.collection.find_one({"_id": ObjectId(object_id)})
    dbdata = json.loads(json_util.dumps(str(data)))
    return dbdata


if __name__ == "__main__":
    app.run(debug=True)
