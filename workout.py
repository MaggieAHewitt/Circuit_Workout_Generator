import math
import csv
from random import shuffle
from circuit import Circuit
from exercise import Exercise


class Workout:
    def __init__(self, all_exercises, num_of_circuits, num_of_exerecises, focus, no_weights, no_stability_ball, no_machines):
        self.circuits = []
        self.focus = focus
        self.focus_ratio = .75  # todo - move to settings file
        self.num_of_circuits = num_of_circuits
        self.num_of_exerecises = num_of_exerecises
        self.no_weights = no_weights
        self.no_stability_ball = no_stability_ball
        self.no_machines = no_machines
        self.setExerciseList(all_exercises)
        self.createWorkout()

    def __str__(self):
        string = ''
        count = 1
        for circuit in self.circuits:
            string += '\n\n--- Circuit ' + str(count) + ' ---'
            string += str(circuit)
            count += 1
        return string

    def createWorkout(self):
        total_exercises_in_workout = self.num_of_circuits * self.num_of_exerecises
        if(total_exercises_in_workout > len(self.filtered_exercise_list)):
            self.printNoWorkoutMessage()
            return

        self.getCircuits()

    def getCircuits(self):
        focus_goal = (math.floor(self.focus_ratio * self.num_of_circuits * self.num_of_exerecises)) if (self.focus != '') else 0
        while (self.num_of_circuits > 0):
            circuit = Circuit(self.filtered_exercise_list, self.num_of_exerecises, self.focus, focus_goal, self.no_weights, self.no_stability_ball, self.no_machines)
            self.circuits.append(circuit)
            self.num_of_circuits -= 1
            focus_goal -= circuit.focused_count

    def setExerciseList(self, all_exercises):
        self.filterExerciseList(all_exercises)
        shuffle(self.filtered_exercise_list)

    def filterExerciseList(self, all_exercises):
        self.filtered_exercise_list = []
        for exercise in all_exercises:
            filter_exercise = False
            if (self.no_weights is True) and (exercise.requires_weights is True):
                filter_exercise = True
            if (self.no_stability_ball is True) and (exercise.requires_stability_ball):
                filter_exercise = True
            if (self.no_machines is True) and (exercise.requires_machine is True):
                filter_exercise = True
            if filter_exercise is False:
                self.filtered_exercise_list.append(exercise)

    def printNoWorkoutMessage(self):
        print("\n OOPS!")
        print("It seems there are no workouts that match the provided criteria.")
        print("Please try again\n")


def loadExercises():
    exercises = []
    file = open('ExerciseList.csv')
    csv_file = csv.reader(file)

    for row in csv_file:
        exercise = Exercise(row[0], row[1], row[2], row[3], row[4], (row[5] if (len(row) > 5) else False))
        exercises.append(exercise)
        print(exercise)

    return exercises
