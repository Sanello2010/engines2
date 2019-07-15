from django.shortcuts import render
from django.http import HttpResponse

def mainpage_index(request):
    return render(request, 'mainpage/mainpage_index.html')
    return HttpResponse("<h3>Hello world</h3>")

# Create your views here.
