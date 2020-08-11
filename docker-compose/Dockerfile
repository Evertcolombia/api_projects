FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
# Install gcc and otrher dependencies
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# Add metadata to the image to describe that the container is listening on port 5000
EXPOSE 5000
COPY . .
# set default command for the container  flask run
CMD ["flask", "run"]
