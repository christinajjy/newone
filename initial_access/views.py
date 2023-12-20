from django.shortcuts import render
from .models import initaccess
from .models import privescalation
from .models import commandcontrol
from .models import credentialaccess
from .models import impact
from .models import execution
from .models import collections
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib
import numpy as np
from django.http import HttpResponse
matplotlib.use('agg')

def home(request):
    return render(request, 'initial_access/index-2.html', {})

def modules(request):
    return render(request, 'initial_access/portfolio.html',{})

def quiz1(request):
    questions = initaccess.objects.all()
    return render(request,'initial_access/initial.html',{
        'questions': questions,
    })

def quiz2(request):
    quest = privescalation.objects.all()
    return render(request,'initial_access/priv.html',{
        'quest': quest,
    })

def quiz3(request):
    qu = commandcontrol.objects.all()
    return render(request,'initial_access/cac.html',{
        'qu': qu,
    })

def quiz4(request):
    ques = credentialaccess.objects.all()
    return render(request, 'initial_access/credaccess.html',{
        'ques': ques,
    })

def quiz5(request):
    qq = impact.objects.all()
    return render(request,'initial_access/impact.html', {
        'qq':qq,
    })

def quiz6(request):
    que = execution.objects.all()
    return render(request,'initial_access/exec.html', {
        'que':que,
    })

def quiz7(request):
    questy = collections.objects.all()
    return render(request,'initial_access/collect.html', {
        'questy':questy,
    })

def result_init(request):
    if request.method == 'POST':
        print(request.POST)
        question= initaccess.objects.all()
        score=0
        wrong=0
        correct=0
        total = question.count()
        temp = total
        for q in question:
            question_value= request.POST.get(q.question)
            option_A_value = 'option_A'  # Use the correct form field name
            option_B_value = 'option_B'
            # Check if the selected option matches the correct option
            if option_A_value == question_value:
                score+=temp
                correct+=1
            elif option_B_value == question_value:
                score-=temp
                wrong+=1
            temp-=1
            total+=temp
        percent = ((score/total)*100)

        labels = ['Complied', 'Not Complied']
        sizes = [correct, wrong]
        explode = (0.1, 0)  # explode 1st slice

        fig1, ax1 = plt.subplots()
        #ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

        # Save the chart to a BytesIO buffer
        chart_buffer = BytesIO()
        plt.savefig(chart_buffer, format='png')
        chart_buffer.seek(0)
        chart_data = base64.b64encode(chart_buffer.getvalue()).decode('utf-8')
        plt.close()

        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
            'chart_data': chart_data,
        }
        return render(request,'initial_access/result_init.html',context)
    else:
        question=initaccess.objects.all()
        context = {
            'question':question
        }
        return render(request,'initial_access/result_init.html',context)
    
def result_init1(request):
    if request.method == 'POST':
        print(request.POST)
        question= privescalation.objects.all()
        score=0
        wrong=0
        correct=0
        total = question.count()
        temp = total
        for q in question:
            question_value= request.POST.get(q.question)
            option_A_value = 'option_A'  # Use the correct form field name
            option_B_value = 'option_B'
            # Check if the selected option matches the correct option
            if option_A_value == question_value:
                score+=temp
                correct+=1
            elif option_B_value == question_value:
                score-=temp
                wrong+=1
            temp-=1
            total+=temp
        percent = ((score/total)*100)
        labels = ['Complied', 'Not Complied']
        sizes = [correct, wrong]
        explode = (0.1, 0)  # explode 1st slice

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

        # Save the chart to a BytesIO buffer
        chart_buffer = BytesIO()
        plt.savefig(chart_buffer, format='png')
        chart_buffer.seek(0)
        chart_data = base64.b64encode(chart_buffer.getvalue()).decode('utf-8')
        plt.close()

        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
            'chart_data': chart_data,
        }
        return render(request,'initial_access/result_init1.html',context)
    else:
        question=privescalation.objects.all()
        context = {
            'question':question
        }
        return render(request,'initial_access/result_init1.html',context)