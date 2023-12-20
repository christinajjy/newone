from django.shortcuts import render
from .models import initaccess
from .models import privescalation
from .models import commandcontrol
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



def result_init(request):
    if request.method == 'POST':
        print(request.POST)
        question = initaccess.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        temp=total
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
        keywords = [question.keywords for question in question]

        # Counting occurrences of each keyword
        keyword_count = {}
        for keyword_list in keywords:
            for keyword in keyword_list.split(','):  # Assuming keywords are separated by comma
                keyword_count[keyword.strip()] = keyword_count.get(keyword.strip(), 0) + 1

        # Sorting the keywords by count
        sorted_keywords = sorted(keyword_count.items(), key=lambda x: x[1], reverse=True)

        # Extracting data for the chart
        top_keywords = [x[0] for x in sorted_keywords[:10]]  # Top 10 keywords
        counts = [x[1] for x in sorted_keywords[:10]]
        labels = ['Complied', 'Non-Complied']
        explode = (0.1, 0)  # explode 1st slice

        fig1, ax1 = plt.subplots(1, 2, figsize=(12, 6))
        sizes = [correct, total - correct]

        sizes = np.nan_to_num(sizes)
        # Pie chart
        ax1[0].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

        # Bar chart
        ax1[1].barh(top_keywords, counts)
        ax1[1].set_xlabel('Count')

        # Save the chart to a BytesIO buffer
        chart_buffer = BytesIO()
        plt.savefig(chart_buffer, format='png')
        chart_buffer.seek(0)
        chart_data = base64.b64encode(chart_buffer.getvalue()).decode('utf-8')
        plt.close()

        context = {
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total,
            'chart_data': chart_data,
            #'chart_image': chart_image,
        }


        return render(request,'initial_access/result_init.html',context)
    else:
        question=initaccess.objects.all()
        context = {
            'question':question
        }
        return render(request,'initial_access/result_init.html',context)

