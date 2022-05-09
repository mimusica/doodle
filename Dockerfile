FROM python:3.10-slim-bullseye
LABEL org.opencontainers.image.source=https://github.com/mimusica/doodle

COPY . /opt/challenge/

WORKDIR /opt/challenge/

RUN python3 -m pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD [ "./app.py" ]
