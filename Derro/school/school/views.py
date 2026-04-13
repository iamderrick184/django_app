from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>welcome</h1>')

def Peter(request):
    return HttpResponse('<h1> My name is Derrick</h1>')

def john(request):
    return HttpResponse('<h2> Muyindi is tall</h2>')