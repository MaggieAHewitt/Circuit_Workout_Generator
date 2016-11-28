import sys
import csv
from exercise import Exercise
from workout import *


def main():

    exercises = loadExercises()

    number_of_circuits = raw_input("Number of Circuits: ")
    exercises_per_circuit = raw_input("Exercises per Circuit: ")
    focus = raw_input("Focus?: ")
    weights = raw_input("Do you have access to weights? (y/n)")
    stability_ball = raw_input("Do you have access to a stability ball? (y/n)")
    machines = raw_input("Do you have access to exercise machines? (y/n)")

    no_weights = True if (weights != 'y') else False
    no_stability_ball = True if (stability_ball != 'y') else False
    no_machines = True if (machines != 'y') else False

    workout = Workout(exercises, int(number_of_circuits), int(exercises_per_circuit), focus, no_weights, no_stability_ball, no_machines)
    print(workout)

if __name__ == "__main__":
    main()
