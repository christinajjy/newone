from django.shortcuts import render
<<<<<<< HEAD
from .models import *

# Create your views here.
def quiz1(request):
    
    
    return render(request, 'initial.html', {})
=======
from .models import initaccess

# Create your views here.
def quiz1(request):
    questions = initaccess.objects.all()
    return render(request,'initial_access/initial.html',{
        'questions': questions,
    })
>>>>>>> 0cd6b5e6284055f5780ea1203563c192080a7863
