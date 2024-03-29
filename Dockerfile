FROM python:3.9.6

RUN mkdir /code
WORKDIR /code

RUN apt-get update -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

#ARG DJANGO_PORT
#EXPOSE 8000
#CMD ["python", "manage.py", "migrate", "&&", "python", "manage.py", "runserver", "0.0.0.0:8000"]
