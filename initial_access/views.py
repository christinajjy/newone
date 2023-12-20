from django.shortcuts import render
from .models import initaccess
from .models import privescalation
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib
matplotlib.use('agg')

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
        total=0
        for q in question:
            total+=1
            print(request.POST.get(q.question))
            if q.option_A ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                score-=10
                wrong+=1
        percent = 100 - (score/(total*10) *100)

        
        labels = ['Correct', 'Wrong']
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