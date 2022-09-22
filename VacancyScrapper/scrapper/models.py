from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=128)
    vacancy_link = models.URLField(max_length=200)
    company = models.CharField(max_length=256)
    location = models.CharField(max_length=128)
    cat = models.ForeignKey('JobCategory', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class JobCatManager(models.Manager):
    def crate_cat(self, name):
        cat = self.create(job_category=name)
        return cat


class JobCategory(models.Model):
    job_category = models.CharField(max_length=128, db_index=True)

    objects = JobCatManager()

    def __str__(self):
        return self.job_category
