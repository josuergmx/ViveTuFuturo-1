from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail,EmailMultiAlternatives
from django.contrib import messages
from django.conf import settings

def principal(request):
    if request.method == 'POST':
        message = request.POST.get('mensaje', '')
        from_email = request.POST.get('mail', '')
        subject = from_email
        to = settings.EMAIL_HOST_USER
        html_content = '<p> hola <strong>'+message+'</strong>.</p>'
        print(message)
        print(from_email)
        if message and from_email:
            try:
                msg = EmailMultiAlternatives(subject,message,to,[to])
                msg.attach_alternative(html_content,"text/html")
                msg.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')
    return render(request,"hola.html",)
