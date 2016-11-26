from exercise import Exercise

# Todo - Move to config file
max_focus_per_circuit = 2


class Circuit:
    def __init__(self, all_exercises, exercises_per_circuit, focus, focus_goal, no_weights, no_stability_ball, no_machines):
        self.focused_count = 0
        self.focus_goal = focus_goal
        self.exercises = []
        self.getExerciseList(all_exercises, exercises_per_circuit, focus, no_weights, no_stability_ball, no_machines)

    def __str__(self):
        string = ''
        for exercise in self.exercises:
            string += str(exercise)
        return string

    # todo - account for weights and stability ball
    def getExerciseList(self, all_exercises, exercises_per_circuit, focus, no_weights, no_stability_ball, no_machines):

        while(exercises_per_circuit > 0):
            if (focus != '') and (self.focus_goal > 0):
                self.getNextFocusedExercise(all_exercises, focus)
                self.focus_goal -= 1

            else:
                self.getNextExercise(all_exercises)

            exercises_per_circuit -= 1

    def getNextExercise(self, all_exercises):
        exercise = all_exercises[0]
        self.exercises.append(exercise)
        all_exercises.pop(0)

    def getNextFocusedExercise(self, all_exercises, focus):
        for exercise in all_exercises:
            if(exercise.group == focus or exercise.secondary_group == focus):
                self.exercises.append(exercise)
                self.focused_count += 1
                all_exercises.remove(exercise)
                return

        # If there aren't any more exercises of that focus, get a generic one
        self.getNextExercise(all_exercises)
