from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the timeclock index.")

def punch(request):
    return HttpResponse("Hello, you are at the Punch In/Out Page")
