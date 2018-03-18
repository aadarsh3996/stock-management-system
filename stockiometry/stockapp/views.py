from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

app_name='stockapp'

def home(request):

    return render(request,'templates/main.html')
