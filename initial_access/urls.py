from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('modules/',views.modules, name='modules'),
    path('q1/',views.quiz1, name='initial_access'),
    path('q2/',views.quiz2, name='priv_escalate'),
    path('result/', views.result, name='result'),
    path('result2/', views.result2, name='pri_result')
]