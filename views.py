from django.views.generic import ListView
from . models import survey

class surveyListView(ListView):
    model = survey
    template_name = 'survey.html'
# Create your views here.
