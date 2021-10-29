import datetime

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    x = datetime.datetime.now()
    return str(x)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)