# Exchange rates v2

**(!)Проект выполнен в рамках тестового задания(!)**  
**Cервис, выдающий текущий курс валюты и историю изменения курса, с доступом только для авторизованных пользователей.**  
**Запущенный сервис каждый день автоматически обновляет данные о курсе валют и сохраняет историю.**  

## Запуск приложения:
1) [Установите Docker](https://www.docker.com/products/docker-desktop)
2) [Установите docker-compose](https://docs.docker.com/compose/install/)
3) Клонируйте репозиторий с проектом:
```
https://github.com/sidorenkov-v-a/exchange_rates_v2.git
```
3) В корневой директории проекта создайте файл `.env`, в котором пропишите переменные окружения  
>Список необходимых переменных можно найти в файле `.env.example`
4) Перейдите в директорию проекта и запустите приложение
```
docker-compose up
```
5) [Документация API](http://127.0.0.1/swagger/) будет доступна по адресу http://127.0.0.1/swagger/

## Дополнительные возможности
- Войдите в контейнер
```
docker exec -it exchange_rates_v2_web_1 bash
```
- Создайте суперпользователя
```
python manage.py createsuperuser
```
- Обновите данные о курсах валют
```
python manage.py update_rates
```

## Стек технологий:   
- Django framework 3.2.6
- Django rest framework 3.12.4
- Redis 6.2.5
- Celery 5.1.2
- PostgreSQL 12.4
- Gunicorn 20.1.0
- Nginx 1.19.0
- Docker, docker-compose

#### Об авторе:
[Профиль Github](https://github.com/sidorenkov-v-a/)  
[Telegram](https://t.me/sidorenkov_vl)
