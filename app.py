from flask import Flask, request, redirect, render_template, url_for
from workout import *

app = Flask(__name__)

all_exercises = loadExercises()
print(str(len(all_exercises)))


@app.route("/")
def index(name=None):
    return render_template('workout_form.html', name='Home')


@app.route("/workout")
def workout(name=None):
    return render_template('workout_list.html', name='Workout')


@app.route("/generate", methods=['POST'])
def generate():
    num_of_circuits = request.form['numberOfCircuits']
    print('num_of_circuits ' + str(num_of_circuits))
    num_of_exerecises = request.form['numberOfExercisesPerCercuit']
    print('num_of_exerecises ' + str(num_of_exerecises))
    focus = '' if (request.form['focus'] == 'ALL') else request.form['focus']
    print('focus ' + focus)

    no_weights = True
    no_stability_ball = True
    no_machines = True

    if request.form.get('weightsAvailable'):
        no_weights = False
    if request.form.get('stabilityBallAvailable'):
        no_stability_ball = False
    if request.form.get('exerciseMachinesAvailable'):
        no_machines = False

    print(str(no_weights))
    print(str(no_stability_ball))
    print(str(no_machines))
    print('all exercises ' + str(len(all_exercises)))

    workout = Workout(all_exercises, int(num_of_circuits), int(num_of_exerecises), focus, no_weights, no_stability_ball, no_machines)

    print(workout)
    return redirect(url_for('workout'))


if __name__ == "__main__":
    app.run()
