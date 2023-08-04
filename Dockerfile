FROM python:3.9-bullseye
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install git
RUN apt-get -y install python3-dev
RUN git --version
RUN python --version
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD ["python3", "test.py"]