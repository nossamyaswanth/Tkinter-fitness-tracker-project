# ACEest Fitness and Gym Tracker

## Overview
This is a simple fitness tracker desktop application built using Tkinter, allowing users to add and view workouts with durations.

## Project Files
- `ACEest_Fitness.py`: Main Tkinter application.
- `tracker_logic.py`: Workout logic separated for unit testing.
- `test_tracker_logic.py`: Pytest unit tests.
- `requirements.txt`: Project dependencies.
- `Dockerfile`: To containerize the app and run tests.
- `.github/workflows/main.yml`: GitHub Actions workflow for CI/CD pipeline.

## How to Run Locally

### Run the application
python ACEest_Fitness.py
### Run tests
pytest test_tracker_logic.py

## CI/CD Pipeline
- The GitHub Actions pipeline automatically runs tests on every push or pull request to the `main` branch.
- It installs dependencies specified in `requirements.txt` and runs pytest on the logic tests.

---
