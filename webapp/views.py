from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
import random
import psutil

all_colors = ["pink", "green", "cadetblue", "plum", "purple"]


def members(request):
    random_color = random.choice(all_colors)
    now = datetime.now()
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    return render(request, "first.html", {"date" : now, "cpu" : cpu_usage, "ram" : ram_usage, "bg_color" : random_color})
