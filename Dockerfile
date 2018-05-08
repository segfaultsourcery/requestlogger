FROM python:3.6-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["gunicorn", "app:app", "--threads=2", "--workers=4", "--bind=0.0.0.0:8000"]