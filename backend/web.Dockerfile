FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

CMD python manage.py migrate --noinput && python manage.py collectstatic --noinput && python manage.py initadmin && python manage.py populate_data && python manage.py runserver 0.0.0.0:8800