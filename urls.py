from django.urls import path
from . import views

urlpatterns = [
    path('', views.surveyListView.as_view(), name='survey'),
]