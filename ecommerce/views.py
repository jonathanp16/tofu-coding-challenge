from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, you are at the ecommerce index page. Good luck!")