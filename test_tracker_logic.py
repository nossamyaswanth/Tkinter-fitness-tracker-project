import pytest
from tracker_logic import FitnessTrackerLogic

def test_add_workout_success():
    tracker = FitnessTrackerLogic()
    tracker.add_workout("Running", "30")
    assert tracker.get_workouts() == [{"workout": "Running", "duration": 30}]

def test_add_workout_missing_fields():
    tracker = FitnessTrackerLogic()
    with pytest.raises(ValueError):
        tracker.add_workout("", "30")
    with pytest.raises(ValueError):
        tracker.add_workout("Running", "")

def test_add_workout_invalid_duration():
    tracker = FitnessTrackerLogic()
    with pytest.raises(ValueError):
        tracker.add_workout("Running", "abc")

def test_clear_workouts():
    tracker = FitnessTrackerLogic()
    tracker.add_workout("Running", "30")
    tracker.clear_workouts()
    assert tracker.get_workouts() == []