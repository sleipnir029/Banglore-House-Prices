from urllib import response
from flask import Flask, request,  jsonify
app = Flask(__name__)

@app.route('/get_location_name')
def get_location_names():
    response = jsonify({
        'location': util.get_location_names()
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response



if __name__ == "__main__":
    print("Starting Python Flask Server for Home Price Prediction")
    app.run()