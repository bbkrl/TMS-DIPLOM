from django.urls import path


# from scrapper.api.v1.endpoints import VacancyView
from scrapper.views import JobView

urlpatterns = [
    # path('v1/job/<str:text>/', VacancyView.as_view()),
    path('', JobView.as_view(), name="job")
]
