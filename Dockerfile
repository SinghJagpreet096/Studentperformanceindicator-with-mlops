FROM python:3.10

COPY src .
COPY artifacts/model.pkl .
COPY artifacts/preprocessor.pkl .
COPY templates .
COPY application.py .
COPY requirements.txt .


WORKDIR /app


RUN pip install -r requirements.txt
CMD python application.py
