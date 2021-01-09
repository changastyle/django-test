from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Holaa")

def chau(request):
    return HttpResponse("Chau amigo!")