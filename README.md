# ACEest Fitness and Gym Tracker

## Overview
This is a simple fitness tracker web application built using Flask, allowing users to add and view workouts with durations. The project demonstrates DevOps practices including version control, unit testing, containerization, and CI/CD automation.

## Project Files
- `app.py`: Main Flask web application.
- `tracker_logic.py`: Core workout logic separated for unit testing.
- `test_tracker_logic.py`: Pytest unit tests for the logic.
- `requirements.txt`: Project dependencies.
- `Dockerfile`: Containerizes the Flask app.
- `.github/workflows/main.yml`: GitHub Actions workflow for CI/CD pipeline.

## How to Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Flask application
```bash
python app.py
```
The app will be available at `http://localhost:5000`.

### 3. Run tests locally
```bash
pytest test_tracker_logic.py
```
This will execute all unit tests for the core logic.

## API Endpoints

- `POST /workout`  
  Add a workout.  
  Example JSON:  
  ```json
  {
    "workout": "Running",
    "duration": "30"
  }
  ```

- `GET /workouts`  
  View all logged workouts.

## Docker Usage

To build and run the app in Docker:
```bash
docker build -t aceest-fitness-app .
docker run -p 5001:5001 aceest-fitness-app
```

## CI/CD Pipeline

- The GitHub Actions pipeline automatically runs tests and builds the Docker image on every push to the `main` branch.
- It installs dependencies, runs pytest, and builds the Docker container to ensure code quality and deployment readiness.

---