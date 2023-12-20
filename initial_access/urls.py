from django.urls import path
from . import views

urlpatterns = [
    path('q1/',views.quiz1, name='initial_access'),
    path('q2/',views.quiz2, name='priv_escalate'),
    path('result_init/', views.result_init, name='result_init'),
    #path('startquiz',views.start_quiz,name="start_quiz"),

]