from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def index(name=None):
    return render_template('index.html', name='Home')


if __name__ == "__main__":
    app.run()