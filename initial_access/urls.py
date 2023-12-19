from django.urls import path
from . import views

urlpatterns = [
    path('q1/',views.quiz1, name='initial_access')
]