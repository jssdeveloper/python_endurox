FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5100
CMD ["uvicorn", "main:app","--workers","13","--reload","--host","0.0.0.0","--port","5100"]
