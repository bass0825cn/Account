from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "adslkfl;aADsAdfD;jadDFsuf  poqlwerj"
app.config.from_object('config')
db = SQLAlchemy(app)

# @app.before_request
# def before_request():
#     g.db = connect_db()


# @app.teardown_request
# def teardown_request(exception):
#     g.db.close()

from Views import *


if __name__ == '__main__':
    app.run(debug=True)
