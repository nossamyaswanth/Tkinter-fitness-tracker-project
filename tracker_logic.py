class FitnessTrackerLogic:
    """
    Core logic for managing fitness workouts.
    """

    def __init__(self):
        self.workouts = []

    def add_workout(self, workout, duration_str):
        if not workout or not duration_str:
            raise ValueError("Workout and duration required")
        try:
            duration = int(duration_str)
        except ValueError:
            raise ValueError("Duration must be a number")
        self.workouts.append({"workout": workout, "duration": duration})

    def get_workouts(self):
        return self.workouts

    def clear_workouts(self):
        self.workouts = []