FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["gunicorn","-w","13","--bind","0.0.0.0:5000","wsgi:app"]s