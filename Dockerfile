FROM python:3.9-buster

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]

#build docker imaged
#docker build -t my-flask-app .
#docker images
# docker run -p 5000:5000 addcae3fe9b5
# https://youtu.be/kBWCsHEcWnc?si=ptwjNUZrqRkV7KJn&t=1391


