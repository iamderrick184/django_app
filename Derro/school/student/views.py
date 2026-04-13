from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app_index(request):
    return render(request,'index.html')
    #return HttpResponse('<h1> Mugaga ate Lulu</h1>')

def app_info(request):
    return HttpResponse('<h1> yoooooooooo</h1>')