import math
from random import shuffle
from circuit import Circuit

# Todo - move to config file, ratio of focused exercises
focusRatio = .75


def createWorkout(all_exercises, num_of_circuits, num_of_exerecises, focus, no_weights, no_stability_ball, no_machines):
    print("\n... Creating a Workout ....\n")

    filtered_exercise_list = filterExerciseList(all_exercises, no_weights, no_stability_ball, no_machines)
    shuffle(filtered_exercise_list)
    total_exercises_in_workout = num_of_circuits * num_of_exerecises

    if(total_exercises_in_workout > len(filtered_exercise_list)):
        print("\n OOPS!")
        print("It seems there are no workouts that match the provided criteria.")
        print("Please try again\n")
        return

    count = 0
    focus_goal = (math.floor(focusRatio * num_of_circuits * num_of_exerecises)) if (focus != '') else 0

    while (num_of_circuits > 0):
        circuit = Circuit(filtered_exercise_list, num_of_exerecises, focus, focus_goal, no_weights, no_stability_ball, no_machines)

        focus_goal -= circuit.focused_count
        count += 1
        num_of_circuits -= 1

        print ('\n\n--- Circuit ' + str(count) + ' ---')
        print(circuit)


def filterExerciseList(all_exercises, no_weights, no_stability_ball, no_machines):
    result = []
    for exercise in all_exercises:
        filter_exercise = False
        if (no_weights is True) and (exercise.requires_weights is True):
            filter_exercise = True
        if (no_stability_ball is True) and (exercise.requires_stability_ball):
            filter_exercise = True
        if (no_machines is True) and (exercise.requires_machine is True):
            filter_exercise = True
        if filter_exercise is False:
            result.append(exercise)
    return result
