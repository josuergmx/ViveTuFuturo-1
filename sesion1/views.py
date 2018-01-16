from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import get_user
#from django.core.mail import send_mail,EmailMessage
#from django.conf import settings
#from . import forms as f
#from . import models as m
#from django.contrib import messages


@login_required(redirect_field_name='login:login')
def sesion1(request):
        return render(request,'sesion1/sesion1.html')
