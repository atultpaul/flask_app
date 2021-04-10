FROM python:3.8-alpine
WORKDIR /docker-flask-test
COPY . /docker-flask-test
RUN pip install -r requirements.txt
CMD ["python","app.py"]