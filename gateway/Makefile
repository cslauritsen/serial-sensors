all: run

rebuild: Dockerfile config.py config.yaml requirements.txt serial2mqtt.py 
	touch rebuild

build: rebuild
	docker build -t serial2mqtt .

stop:
	docker rm -f serial2mqtt

run:
	docker run --rm -d \
		--name serial2mqtt \
		--device=/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_7543331373935161D021-if00:/dev/arduino \
		-v $(PWD):/app \
		--pull always \
		registry.ingress.planetlauritsen.com/serial2mqtt:latest
push:  build
	docker tag serial2mqtt registry.ingress.planetlauritsen.com/serial2mqtt:latest
	docker push registry.ingress.planetlauritsen.com/serial2mqtt:latest

rsync:
	rsync -Pvaz .. ub:repos/SerialSensors