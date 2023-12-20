from django.shortcuts import render
from .models import initaccess
from .models import privescalation
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib
from django.http import HttpResponseRedirect
matplotlib.use('agg')

def q1(request):
    questions = initaccess.objects.all()
    return render(request,'initial_access/initial.html',{
        'questions': questions,
    })

def q2(request):
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
        return render(request,'initial_access/result.html',context)
    else:
        question=initaccess.objects.all()
        context = {
            'question':question
        }
        return render(request,'initial_access/priv.html',context)

def start_quiz(request):
    if request.method =='POST':
        return HttpsResponseRedirect('initial_access/initial.html')
    return render(request,"initial_access/quiz_list.html",{})

def quiz1_button(request):
    return render(request,'initial_access/priv.html',{})

from django.shortcuts import render
from django.http import HttpResponseRedirect

def first_page(request):
    if request.method == 'POST':
        # Redirect to another Django view
        return HttpResponseRedirect('/q1/')  # Replace '/another-page/' with your desired URL

    return render(request, 'initial_access/initial.html')

from .models import responses
from django.shortcuts import render
 
def index(request):
  magma_composition_data = [
    {"label":"initial_access_result","symbol":"IAR","y":initial_access_result},
    {"label":"privescalation_result","symbol":"PER","y":privescalation_result},
    {"label":"credentialaccess_result","symbol":"CAR","y":credentialaccess_result},
    {"label":"commandcontrol_result","symbol":"CCR","y":commandcontrol_result},
    
  ]
 
  return render(request, 'index.html', { "magma_composition_data" : magma_composition_data })    



