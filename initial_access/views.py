from django.shortcuts import render
from .models import initaccess
from .models import privescalation
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib
from django.http import HttpResponseRedirect
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

def result(request):
    if request.method == 'POST':
        print(request.POST)
        question= initaccess.objects.all()
        score=0
        wrong=0
        correct=0
        total = question.count()
        for q in question:
            question_value= request.POST.get(q.question)
            option_A_value = 'option_A'  # Use the correct form field name
            option_B_value = 'option_B'
            # Check if the selected option matches the correct option
            if option_A_value == question_value:
                score+=10
                correct+=1
            elif option_B_value == question_value:
                score-=10
                wrong+=1
        percent = 100 - ((score)/(total*10) *100)

        
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
        return render(request,'initial_access/result.html',context)
    else:
        question=quiz1.objects.all()
        context = {
            'question':question
        }
        return render(request,'initial_access/priv.html',context)

def result2(request):
    if request.method == 'POST':
        print(request.POST)
        quest= privescalation.objects.all()
        score=0
        wrong=0
        correct=0
        total = quest.count()
        for q in quest:
            question_value= request.POST.get(q.question)
            option_A_value = 'option_A'  # Use the correct form field name
            option_B_value = 'option_B'
            # Check if the selected option matches the correct option
            if option_A_value == question_value:
                score+=10
                correct+=1
            elif option_B_value == question_value:
                score-=10
                wrong+=1
        if total == 0:
            percent = float('nan')
        else:
            percent = 100 - ((score)/(total*10) *100)

        
        labels = ['Complied', 'Not Complied']
        sizes = [correct, wrong]
        explode = (0.1, 0)  # explode 1st slice

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

        # Save the chart to a BytesIO buffer
        chartBuffer = BytesIO()
        plt.savefig(chartBuffer, format='png')
        chartBuffer.seek(0)
        chartData = base64.b64encode(chartBuffer.getvalue()).decode('utf-8')
        plt.close()

        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
            'chart_data': chartData,
        }
        return render(request,'initial_access/result2.html',context)
    else:
        question=quiz1.objects.all()
        context = {
            'question':question
        }
        return render(request,'initial_access/priv.html',context)

