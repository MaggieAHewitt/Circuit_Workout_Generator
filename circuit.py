from random import shuffle
from exercise import Exercise

# Todo - Move to config file
max_focus_per_circuit = 2
add_complimentary_exercises = True

compliments = {'BACK': 'CHEST', 'CHEST': 'BACK', 'CORE': 'BACK', 'BICEPS': 'TRICEPS', 'TRICEPS': 'BICEPS', 'HAMSTRING': 'QUADRICEPS', 'QUADRICEPS': 'HAMSTRING'}


class Circuit:
    def __init__(self, all_exercises, exercises_per_circuit, focus, focus_goal, no_weights, no_stability_ball, no_machines):
        self.focused_count = 0
        self.next_complimentary_exercise = ''
        self.exercises = []
        self.focus_goal = focus_goal
        self.getExerciseList(all_exercises, exercises_per_circuit, focus, no_weights, no_stability_ball, no_machines)

    def __str__(self):
        string = ''
        for exercise in self.exercises:
            string += str(exercise)
        return string

    # todo - account for weights and stability ball
    def getExerciseList(self, all_exercises, exercises_per_circuit, focus, no_weights, no_stability_ball, no_machines):

        while(exercises_per_circuit > 0):
            if (focus != '') and (self.focus_goal > 0) and (self.focused_count < max_focus_per_circuit):
                self.getNextFocusedExercise(all_exercises, focus)
                self.focus_goal -= 1
                self.focused_count += 1

            elif (add_complimentary_exercises is True) and (self.next_complimentary_exercise != ''):
                self.getNextFocusedExercise(all_exercises, self.next_complimentary_exercise)
                self.next_complimentary_exercise = ''

            else:
                self.getNextExercise(all_exercises)

            exercises_per_circuit -= 1

        shuffle(self.exercises)

    def getNextExercise(self, all_exercises):
        exercise = all_exercises[0]
        self.exercises.append(exercise)
        self.setComplimentaryExercise(exercise.group)
        all_exercises.pop(0)

    def getNextFocusedExercise(self, all_exercises, focus):
        for exercise in all_exercises:
            if(exercise.group == focus or exercise.secondary_group == focus):
                self.exercises.append(exercise)
                self.setComplimentaryExercise(focus)
                all_exercises.remove(exercise)
                return

        # If there aren't any more exercises of that focus, get a generic one
        self.getNextExercise(all_exercises)

    def setComplimentaryExercise(self, last_group):
        if (add_complimentary_exercises is True) and (last_group in compliments.keys()):
            self.next_complimentary_exercise = compliments[last_group]
