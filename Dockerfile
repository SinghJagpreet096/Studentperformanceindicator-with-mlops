FROM python:3.10

COPY ./src /app/src
COPY artifacts/model.pkl /app/artifacts/model.pkl
COPY artifacts/preprocessor.pkl /app/artifacts/preprocessor.pkl
COPY ./templates /app/templates
COPY application.py /app/application.py
COPY requirements.txt /app/requirements.txt


WORKDIR /app


RUN pip install -r requirements.txt
CMD python application.py
