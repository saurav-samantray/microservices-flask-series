FROM python:3.6

#RUN apt-get install -y default-libmysqlclient-dev

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt

COPY  . .
