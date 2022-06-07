FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /cooking_site/
RUN pip install -r requirements.txt