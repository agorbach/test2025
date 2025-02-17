FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install --no-cache-dir Flask

EXPOSE 8080
CMD ["python", "/app/main.py"]
