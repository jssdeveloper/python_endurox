FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5200
WORKDIR /app/django_api
CMD ["gunicorn","django_api.wsgi","--bind","0.0.0.0:5200","--workers","13"]