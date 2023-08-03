from datetime import datetime
from time import strftime, gmtime
from django.shortcuts import render

def current_date_time(request):
    context = {
        # "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
        "time": datetime.now
    }
    return render(request, 'index.html', context)
