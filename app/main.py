from flask import Flask
from flask import request
from flask_cors import CORS
import sqlite3
import json
import pickle
# from ML.test_model import irrigate_or_not_irrigate

app = Flask(__name__)

# enable cors
CORS(app)

# load the model from disk
filename = 'irrigate_final_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

def irrigate_or_not_irrigate(Type, Moisture):
    if(loaded_model.predict([[Type, Moisture]]))==0:
        return 'Not irrigate'
    else:
        return 'Irrigate'

@app.route("/")
def home_view():
    return {
        "api_state": "Up and running"
    }


# API working endpoint
@app.post('/api/predict')
def predict():
        # print(request.form.get('Type','soil_moisture'))
        Type = request.form.get('Type')
        Moisture = request.form.get('Moisture')
        typ_to_int = int(Type)
        moisture_to_int = int(Moisture)
        predictions = irrigate_or_not_irrigate(typ_to_int, moisture_to_int)
        return {
            "predictions": predictions
        }




# def greetings():
#     message = ""
#     username = request.form.get('username')
#     timestamp = request.form.get('timestamp')

#     conn = get_db_connection()
#     conn.execute(
#         'INSERT INTO greet (username, created) VALUES (?, ?)', (username, timestamp))
#     conn.commit()
#     conn.close()

#     message = "Hello, " + username

#     # response
#     return {
#         "status": "success",
#         "greet_message": message
#     }


# # returns all the greeted users
# @app.get('/api/users')
# def get_users():
#     conn = get_db_connection()
#     users = conn.execute(
#         'SELECT * FROM greet ORDER BY id DESC LIMIT 10').fetchall()
#     conn.close()

#     return {
#         "users": users
#     }
