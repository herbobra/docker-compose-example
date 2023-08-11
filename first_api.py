from flask import Flask, g, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)



@app.route('/send')
def convert_to_pdf():
    a = "Durak"
    print(a)
    return a    


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True, port=5050)
