FROM python:3.12.4-bullseye

RUN pip install Flask

COPY ./app /app

CMD ["python", "/app/main.py"]
