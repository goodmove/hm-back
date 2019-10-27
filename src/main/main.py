from flask import Flask

import src.main.api.common as common_api
import src.main.api.subjects as subjects_api
import src.main.api.memes as memes_api
import src.main.api.users as users_api
import src.main.api.answers as answers_api

app = Flask(__name__)


@app.route('/')
def index():
    return "Home page content"


common_api.init(app)
subjects_api.init(app)
memes_api.init(app)
users_api.init(app)
answers_api.init(app)


app.run(host='0.0.0.0', port=5000)
