from flask import Flask

import src.main.api.subjects as subjects_api

app = Flask(__name__)


@app.route('/')
def index():
    return "Home page content"


subjects_api.init(app)

app.run(host='0.0.0.0', port=5000)
