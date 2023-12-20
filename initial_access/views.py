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
    # Fetching questions from the model
    questions = initaccess.objects.all()

    # Extracting keywords from questions
    keywords = [question.keywords for question in questions]

    # Counting occurrences of each keyword
    keyword_count = {}
    for keyword_list in keywords:
        for keyword in keyword_list.split(','):  # Assuming keywords are separated by comma
            keyword_count[keyword.strip()] = keyword_count.get(keyword.strip(), 0) + 1

    # Sorting the keywords by count
    sorted_keywords = sorted(keyword_count.items(), key=lambda x: x[1], reverse=True)

    # Extracting data for the chart
    top_keywords = [x[0] for x in sorted_keywords[:10]]  # Top 10 keywords
    counts = [x[1] for x in sorted_keywords[:10]]  # Corresponding counts

    # Creating the bar chart
    plt.figure(figsize=(10, 6))
    plt.barh(top_keywords, counts)
    plt.xlabel('Count')

    # Saving the chart to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    chart_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    # Passing the chart image and other data to the template
    context = {
        'chart_image': chart_image,
    }
    return render(request, 'initial_access/result_init.html', context)

