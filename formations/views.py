from django.shortcuts import render
from django.views.generic import CreateView
from salles.models import Formation
from .forms import FormationForm
# Create your views here.

class FormationCreateView(CreateView):
	model = Formation
	form_class = FormationForm
	template_name = 'formations_add.html'