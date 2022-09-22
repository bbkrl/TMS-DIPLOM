Чтобы запустить проект:

1. pip install -r requirements.txt

2. docker run -d -p 6379:6379 redis
   (чтобы убедиться, что redis работает:
   - redis-cli ping)
3. python manage.py runserver
4. celery -A VacancyScrapper worker -l info (запускать из директории на уровне manage.py)

проект запущен и готов к использованию





