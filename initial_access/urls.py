from django.urls import path
from . import views

urlpatterns = [
    path('q1/',views.landing_page, name='initial_access')
]