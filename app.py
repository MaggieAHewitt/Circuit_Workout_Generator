from flask import Flask, request, redirect, render_template, url_for
from workout import *

app = Flask(__name__)

all_exercises = loadExercises()


@app.route("/")
def index(name=None):
    return render_template('workout_form.html', name='Home')


@app.route("/workout", methods=['GET','POST'])
def workout():

    if request.method == 'GET':
        return redirect('/')

    num_of_circuits = request.form['numberOfCircuits']
    num_of_exerecises = request.form['numberOfExercisesPerCercuit']
    focus = '' if (request.form['focus'] == 'ALL') else request.form['focus']

    no_weights = True
    no_stability_ball = True
    no_machines = True

    if request.form.get('weightsAvailable'):
        no_weights = False
    if request.form.get('stabilityBallAvailable'):
        no_stability_ball = False
    if request.form.get('exerciseMachinesAvailable'):
        no_machines = False

    workout = Workout(all_exercises, int(num_of_circuits), int(num_of_exerecises), focus, no_weights, no_stability_ball, no_machines)

    return render_template('workout_list.html', circuits=workout.circuits)

if __name__ == "__main__":
    app.run()
