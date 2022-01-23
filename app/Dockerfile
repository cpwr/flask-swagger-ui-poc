FROM python:3.6
ENV PYTHONUNBUFFERED 1
COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt

CMD gunicorn -w 3 -b 0.0.0.0:5000 --reload run:app
