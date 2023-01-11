# set base image (host OS)
FROM python:3-slim

LABEL org.opencontainers.image.source=https://github.com/9p4/gradescope-cal-sync

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN apt-get update && apt-get install -y build-essential && pip install -r requirements.txt && apt-get remove -y build-essential && apt-get -y autoremove

# copy the required files to the working directory
COPY gradescope-cal-daemon.py .

# command to run on container start
CMD [ "python", "./gradescope-cal-daemon.py" ] 
