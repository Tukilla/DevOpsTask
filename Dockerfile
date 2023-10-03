# Download python

FROM python:3

#Create and navigate to folder
RUN mkdir app
RUN cd app

WORKDIR /app

ADD pythonapp.py .

CMD ["python", "-u", "pythonapp.py"]
