FROM python:3.10.0
RUN pip install Flask
RUN useradd -ms /bin/bash admin
USER admin
WORKDIR /app
COPY app /app
CMD ["python", "app.py"]
