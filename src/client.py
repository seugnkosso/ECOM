from flask import Flask

app = Flask(__name__)

app.config.from_pyfile("../config.py")

@app.route('/client')
def client():
    return "<h1>client</h1>"