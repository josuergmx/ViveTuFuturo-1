from django.shortcuts import render
from . import forms as f
# Create your views here.

def agenda(request):
    cita = f.agendaForm()
    context = {
        "cita":cita,
    }
    return render(request,"agenda/agenda.html",context)
