from flask import Flask

app = Flask(__name__)


@app.route('/', methods=["GET"])
def root():
    return "<h1>chal be chal nikal</h1>"


app.run(port=4000, host="0.0.0.0")
