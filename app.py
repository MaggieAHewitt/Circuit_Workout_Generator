from flask import Flask, request, redirect, render_template, url_for, session
from workout import *

app = Flask(__name__)

all_exercises = loadExercises()


@app.route("/")
def index(name=None):
    return render_template('workout_form.html', name='Home')


@app.route("/refresh", methods=['GET', 'POST'])
def refresh():
    last_request = session['last_request']

    if((last_request is None) or (request.method == 'GET')):
        return redirect('/')

    num_of_circuits = last_request.get('num_of_circuits')
    num_of_exerecises = last_request.get('num_of_exerecises')
    focus = last_request.get('focus')
    no_weights = last_request.get('no_weights')
    no_stability_ball = last_request.get('no_stability_ball')
    no_machines = last_request.get('no_machines')

    workout = Workout(all_exercises, int(num_of_circuits), int(num_of_exerecises), focus, no_weights, no_stability_ball, no_machines)
    return render_template('workout_list.html', circuits=workout.circuits)

@app.route("/workout", methods=['GET', 'POST'])
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

    last_request = {'num_of_circuits': num_of_circuits, 'num_of_exerecises': num_of_exerecises, 'focus': focus, 'no_weights': no_weights, 'no_stability_ball': no_stability_ball, 'no_machines': no_machines}

    session['last_request'] = last_request
    workout = Workout(all_exercises, int(num_of_circuits), int(num_of_exerecises), focus, no_weights, no_stability_ball, no_machines)
    return render_template('workout_list.html', circuits=workout.circuits)

app.secret_key = '\x96\xa9\xca\xb7.o\xe7:\xd4D\x04\xea\x98\xa9[#"\r`[v\xb9\xa3\xe9'

# Remove for Python Hosting
if __name__ == "__main__":
    app.run()
