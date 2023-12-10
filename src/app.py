from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello to my API, this is the main page (for now)'