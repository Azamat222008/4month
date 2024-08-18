from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hello World!")


def main_page_view(request):
    return render(request, 'main_page.html')
