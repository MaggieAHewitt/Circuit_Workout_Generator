from exercise import Exercise


class Circuit:
    def __init__(self, all_exercises, exercises_per_circuit, focus, focus_goal):
        self.focused_count = 0
        self.exercises = []

        self.getNaiveExerciseList(all_exercises, exercises_per_circuit, focus, focus_goal)

    def __str__(self):
        string = ''
        for exercise in self.exercises:
            string += str(exercise)
        return string

    # todo - account for weights and stability ball
    def getNaiveExerciseList(self, all_exercises, exercises_per_circuit, focus, focus_goal):
        while(exercises_per_circuit > 0):
            if (focus != '') and (focus_goal > 0):
                self.getNextFocusedExercise(all_exercises, focus)
                focus_goal -= 1

            else:
                self.getNextExercise(all_exercises)

            exercises_per_circuit -= 1

    def getNextFocusedExercise(self, all_exercises, focus):
        # Todo - get list of all exercises in focus in order of count
        for exercise in all_exercises:
            if(exercise.group == focus or exercise.secondary_group == focus):
                self.exercises.append(exercise)
                self.focused_count += 1
                all_exercises.remove(exercise)
                return

        # If there aren't any more exercises of that focus, get a generic one
        self.getNextExercise(all_exercises)

    def getNextExercise(self, all_exercises):
        # Todo - get list of all exercises in focus in order of count
        exercise = all_exercises[0]
        self.exercises.append(exercise)
        all_exercises.pop(0)
