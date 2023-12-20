from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('modules/',views.modules, name='modules'),
    path('q1/',views.quiz1, name='initial_access'),
    path('q2/',views.quiz2, name='priv_escalate'),
    path('q3', views.quiz3, name='commandcontrol'),
    path('result_init/', views.result_init, name='result_init'),
    #path('startquiz',views.start_quiz,name="start_quiz"),

]