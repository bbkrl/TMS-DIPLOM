import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VacancyScrapper.settings')

app = Celery('VacancyScrapper')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()