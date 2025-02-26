FROM python:3.12.9-slim

ENV PIP_ROOT_USER_ACTION=ignore
RUN apt-get update && pip install --upgrade pip 



ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /webapp

COPY ./requirements.txt /webapp

RUN pip install --no-cache-dir -r requirements.txt

COPY . /webapp

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
