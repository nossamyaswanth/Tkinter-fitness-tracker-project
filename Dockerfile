FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ACEest_Fitness.py .
COPY tracker_logic.py .
COPY test_tracker_logic.py .

CMD ["pytest", "--maxfail=1", "--disable-warnings", "-q"]