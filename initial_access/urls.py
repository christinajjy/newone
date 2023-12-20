from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('modules/',views.modules, name='modules'),
    path('q1/',views.quiz1, name='initial_access'),
    path('q2/',views.quiz2, name='priv_escalate'),
<<<<<<< HEAD
    path('result_init/', views.result_init, name='result_init'),
    #path('startquiz',views.start_quiz,name="start_quiz"),

=======
    path('result/', views.result, name='result'),
    path('result2/', views.result2, name='pri_result')
>>>>>>> 078458dba0e2e8d1f13d6660dd0712687e8c267e
]