from flask import Flask, g, request
from flask_cors import CORS

import requests

app = Flask(__name__)
CORS(app)



@app.route('/get')
def loh():
    r = requests.get("http://localhost:5050/send")
    print(r.text)
    return str(r.text)+", skazali"    


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True, port=5000)
