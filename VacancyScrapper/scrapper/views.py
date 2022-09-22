from django.shortcuts import render
from django.views.generic import CreateView

from .forms import JobForm
from .models import JobCategory
from .tasks import get_job


class JobView(CreateView):
    """отображение формы по получению вакансий по запросу"""
    model = JobCategory
    form_class = JobForm
    success_url = '/admin/scrapper/vacancy/'
    template_name = 'main/get_job.html'

    def form_valid(self, form):
        form.save()
        get_job.delay(form.instance.job_category)

        return super().form_valid(form)
