from django.http import HttpResponse

def home(request): #vista
    return HttpResponse("<h1>HOLA MUNDO</h1>")

