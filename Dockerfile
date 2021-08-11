FROM python:3.8.5

WORKDIR /code

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD bash -c \
"python manage.py wait_for_db && \
python manage.py migrate && \
python manage.py collectstatic --noinput && \
python manage.py update_rates && \
gunicorn exchange_rates.wsgi:application --bind 0.0.0.0:8000 --timeout 120"
