FROM python:3.9-slim-bullseye
RUN apt-get update
RUN apt-get install pkg-config -y
RUN apt-get install python3-dev default-libmysqlclient-dev libpq-dev build-essential -y
RUN apt-get install -y xvfb
RUN apt-get install -y wget
RUN apt-get install -y openssl
RUN apt-get update
RUN mkdir /dbconstruction
WORKDIR /dbconstruction
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["python", "manage.py" , "runserver", "0.0.0.0:8000"]