from django.shortcuts import render

def index_vid(request):
    return render(request, '/video/index_vid.html')

# Create your views here.
