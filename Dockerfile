FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=teachmeumb.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=${PORT}

CMD ["flask", "run"]
