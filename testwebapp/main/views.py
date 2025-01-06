from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def index(reqest):
    return HttpResponse("HELLLO PYTON!")
def about(reqest):
    return HttpResponse("ABOUT FROM MYWEB!")