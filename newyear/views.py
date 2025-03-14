from django.shortcuts import render
import datetime
def index(request):
    now = datetime.datetime.now()
    context = {"newyear": now.month == 1 and now.day==1}
    return render(request, 'newyear/index.html', context)



# Create your views here.
