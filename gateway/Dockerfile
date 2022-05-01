FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y vim less
RUN apt-get install -y python3-pip
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . . 

CMD ./serial2mqtt.py