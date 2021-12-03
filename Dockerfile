FROM python:3.10-slim-buster
RUN pip3 install --user --no-cache-dir Flask requests gunicorn
WORKDIR /app
COPY app /app
CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app" ]
