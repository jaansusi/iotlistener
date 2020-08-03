FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir mysql-connector-python paho-mqtt pyyaml pytz

COPY . .

CMD ["python", "./main.py"]