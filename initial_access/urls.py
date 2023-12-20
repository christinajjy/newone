from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('modules/',views.modules, name='modules'),
    path('q1/',views.quiz1, name='initial_access'),
    path('q2/',views.quiz2, name='priv_escalate'),
    path('q3/', views.quiz3, name='commandcontrol'),
    path('q4/',views.quiz4, name='credaccess'),
    path('q5/',views.quiz5, name='impact'),
    path('q6/',views.quiz6, name='execution'),
    path('q7/',views.quiz7, name='collection'),
    path('result_init/', views.result_init, name='result_init'),
    path('result_init1/', views.result_init1, name='result_init1'),

]