from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1>this is first response from app2 view1 </h1>')
def second(request):
    return HttpResponse('<h1>this is second response from app2 view2</h1>')