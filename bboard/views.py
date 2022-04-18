from django.http import HttpResponse

def index(request):
    return HttpResponse('здесь будет выведен список обьявлений')