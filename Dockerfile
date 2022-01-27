FROM python:3.10

WORKDIR /

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN mkdir "data"

COPY ./src /src
COPY main.py main.py

CMD [ "python3", "main.py" ]