from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def principal(request):
    if request.method == 'POST':
        message = request.POST.get('mensaje', '')
        from_email = request.POST.get('mail', '')
        subject = 'Prueba'
        print(message)
        print(from_email)
        if message and from_email:
            try:
                send_mail(subject, message, from_email, ['eckobik@gmail.com'], fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')
    return render(request,"hola.html",)
