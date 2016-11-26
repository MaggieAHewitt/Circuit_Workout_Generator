import sys
import csv
from exercise import Exercise
from workout import *


def main():
    exercises = loadExercises()
    numberOfCircuits = raw_input("Number of Circuits: ")
    exercisesPerCircuit = raw_input("Exercises per Circuit: ")
    focus = raw_input("Focus: ")
    createWorkout(exercises, int(numberOfCircuits), int(exercisesPerCircuit), focus)


def loadExercises():
    exercises = []
    file = open('ExerciseList.csv')
    csv_file = csv.reader(file)

    for row in csv_file:
        exercise = Exercise(row[0], row[1], row[2], row[3], row[4])
        exercises.append(exercise)

    return exercises


if __name__ == "__main__":
    main()
