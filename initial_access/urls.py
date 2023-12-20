from django.urls import path
from . import views

urlpatterns = [
    path('q1/',views.q1, name='initial_access'),
    path('q2/',views.q2, name='priv_escalate'),
    path('result/', views.result, name='result'),
    path('startquiz',views.start_quiz,name="start_quiz"),
    path('result/index.html',views.index,name='index'),
]