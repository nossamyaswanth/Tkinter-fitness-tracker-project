import pytest
from tracker_logic import FitnessTrackerLogic

def test_add_workout_success():
    tracker = FitnessTrackerLogic()
    tracker.add_workout('Jogging', '40')
    assert tracker.get_workouts() == [{'workout': 'Jogging', 'duration': 40}]

def test_add_workout_missing_fields():
    tracker = FitnessTrackerLogic()
    with pytest.raises(ValueError):
        tracker.add_workout('', '30')
    with pytest.raises(ValueError):
        tracker.add_workout('Jogging', '')

def test_add_workout_invalid_duration():
    tracker = FitnessTrackerLogic()
    with pytest.raises(ValueError):
        tracker.add_workout('Jogging', 'abc')