from flask import Flask
from transaction import transactionObject

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/create_transaction", methods=["POST"])
def hello_world():
    msg = transactionObject()
    return msg

# app.run()

# gunicorn --bind 0.0.0.0:5000 -w 8 wsgi:app