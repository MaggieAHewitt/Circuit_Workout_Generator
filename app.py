from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)


@app.route("/")
def index(name=None):
    return render_template('workout_form.html', name='Home')


@app.route("/workout")
def workout(name=None):
    return render_template('workout_list.html', name='Workout')


@app.route("/generate", methods=['POST'])
def generate():
    return redirect(url_for('workout'))


if __name__ == "__main__":
    app.run()
