FROM python:3.10-slim-buster
RUN pip3 install --user --no-cache-dir Flask requests
WORKDIR /app
COPY app /app
CMD ["python", "app.py"]
