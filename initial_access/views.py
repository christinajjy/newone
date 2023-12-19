from django.shortcuts import render
from .models import initaccess

# Create your views here.
def quiz1(request):
    questions = initaccess.objects.all()
    return render(request,'initial_access/initial.html',{
        'questions': questions,
    })