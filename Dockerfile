FROM python:3.11

RUN pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt /app/

EXPOSE 8000

RUN pip install -r /app/requirements.txt

COPY . .