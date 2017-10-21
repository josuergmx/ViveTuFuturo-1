from django.shortcuts import render

# Create your views here.

def agenda(request):
    render(request,"agenda.html")
