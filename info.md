Testing Flask, Fastapi, Django and compare to Enduro/X performance.
Flask - https://flask.palletsprojects.com/en/2.3.x/
FastApi - https://fastapi.tiangolo.com/
Django - https://docs.djangoproject.com/en/4.2/
Enduro/X - https://www.endurox.org/

Github repository with project files - https://github.com/jssdeveloper/python_endurox

1. Created simple Flask app, dockerzed it to run on port 5000 with Gunicorn. According to gunicorn worker count should be CPU cores \* 2 + 1 so in this test I use 13 workers.
   Building the docker image with $ docker build -t flask-api .
   Running the docker container with $ docker run -p 5000:5000 flask-api
   Opening http://localhost:5000/ or http://127.0.0.1:5000/ or on local network {local ip}:5000

2. Created simple Fastapi app, dockerized it to run on port 5100 with Uvicorn with 13 workers

3. Created simple Django app, dockerized it to run on port 5200 with Gunicorn & 13 workers.

Test #1: create transaction json object, test with Apache ab: $ ab -c 100 -n 30000 {address}:{port}
