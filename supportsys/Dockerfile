#Pull a base image
FROM python:3.10
#Set environment variables
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1
#Set the work directory
WORKDIR /project1
#Install dependancies
COPY Pipfile Pipfile.lock /project1/
RUN pip  install pipenv && pipenv install --system



#copy project 
COPY . /project1/

