import math
from circuit import Circuit

# The ratio of focused exercises
focusRatio = .75


def createWorkout(all_exercises, num_of_circuits, num_of_exerecises, focus):
    print("\n... Creating a Workout ....\n")
    count = 0
    focus_goal = (math.floor(focusRatio * num_of_circuits * num_of_exerecises)) if (focus != '') else 0

    while (num_of_circuits > 0):
        circuit = Circuit(all_exercises, num_of_exerecises, focus, focus_goal)

        focus_goal -= circuit.focused_count
        count += 1
        num_of_circuits -= 1

        print ('\n\n--- Circuit ' + str(count) + ' ---')
        print(circuit)
