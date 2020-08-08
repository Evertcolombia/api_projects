FROM python:3.7-alpine
MAINTAINER EvertColombia

#recomended in containers
#avoid  python to buffer the outputs, prints it directly
ENV PYTHONUNBUFFERED 1

# Install all dependecies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Make folder to store application
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# User that's going to run app -D
RUN adduser -D user
USER user
