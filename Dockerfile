# installed a lightweight operating system
From python:3.8
# any python output for example an error send asap to docker terminal
# normally information is buffered and send to when it reaches a point.
ENV PYTHONUNBUFFERED=1
# created a directory called app
WORKDIR /django
# copied requirements.txt file into this directory and name it requirements.txt
COPY requirements.txt /django/requirements.txt
# install requirements.txt file
RUN pip install -r requirements.txt
# copy the folder that we are in into the app folder. copy everything.
COPY . /django