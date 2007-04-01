from django.urls import path
from . import views

app_name = 'formations'

urlpatterns = [
    path('add/', views.FormationCreateView.as_view(), name='add'),
]