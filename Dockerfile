
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y git wget pv jq python3-dev ffmpeg mediainfo && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
