from flask import Flask, request, jsonify
from tracker_logic import FitnessTrackerLogic

app = Flask(__name__)
tracker = FitnessTrackerLogic()

@app.route('/workout', methods=['POST'])
def add_workout():
    data = request.get_json()
    workout = data.get('workout')
    duration = data.get('duration')
    try:
        tracker.add_workout(workout, duration)
        return jsonify({"message": "Workout added successfully"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/workouts', methods=['GET'])
def get_workouts():
    return jsonify(tracker.get_workouts()), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)