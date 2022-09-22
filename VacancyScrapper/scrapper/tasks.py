from VacancyScrapper.celery import app

# from scrapper.api.v1.serializers import JobSerializer
from scrapper.models import Vacancy, JobCategory
from services.headhunter import get_jobs


@app.task
def get_job(job_name):
    cat = JobCategory.objects.crate_cat(job_name)
    vacancy_list = get_jobs(job_name)
    for item in vacancy_list:
        Vacancy.objects.create(title=item['title'],
                               vacancy_link=item['vacancy_link'],
                               company=item['company'],
                               location=item['location'],
                               cat=cat)
