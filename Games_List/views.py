import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, Django!")

def test_code(request, name):
    print(request.build_absolute_uri())
    
    return render(
        request, 
        'Games_List/test.html', 
        {
            'name' : name,
            'date' : datetime.now()
            
        }
    )