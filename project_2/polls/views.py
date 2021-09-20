from django.http import HttpResponse
from django.shortcuts import render
import datetime


def index(request):
    num = 410230
    percentage = 70
    days = 30
    return render(request, 'polls/index.html', context={'number': num, 'percentage': percentage, 'days': days})
