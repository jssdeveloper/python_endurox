from flask import Flask
from transaction import transactionObject

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def hello_world():
    msg = transactionObject()
    return msg