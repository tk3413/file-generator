FROM python:3.9

WORKDIR /app

COPY . .

RUN apt-get update && apt-get upgrade -y
RUN pip3 install -r requirements.txt

ENTRYPOINT python3 src/file_generator.py
