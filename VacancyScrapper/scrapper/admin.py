from django.contrib import admin

from scrapper.models import Vacancy, JobCategory


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'vacancy_link', 'cat')
    list_filter = ('title', 'location', 'cat')
    search_fields = ('company',)


@admin.register(JobCategory)
class JobCatAdmin(admin.ModelAdmin):
    list_display = ('job_category',)
