FROM python

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app
COPY docker-compose.yml /app
COPY main.py /app
COPY . /app

RUN pip install --no-cache-dir yt-dlp

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
