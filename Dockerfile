FROM python:3.10

COPY src/ /app
COPY artifacts/model.pkl /app
COPY artifacts/preprocessor.pkl /app
COPY templates/ /app
COPY application.py /app
COPY requirements.txt /app


WORKDIR /app


RUN pip install -r requirements.txt
CMD python application.py
