FROM python:3.6

ENV PYTHONUNBUFFERED 1

COPY . /code/
WORKDIR /code/


RUN pip install pipenv
RUN pipenv install --system && pipenv install --dev --system

RUN cp /code/env.tmpl /code/snc/.env
RUN python /code/manage.py migrate
RUN python /code/manage.py collectstatic --noinput


EXPOSE 8000

CMD ["python","/code/manage.py","runserver","0.0.0.0:8000"]
