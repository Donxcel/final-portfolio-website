# importing the main libraries from django needed for the view.py
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def homepage(request):
    return render(request,'index.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            # we use the django default built in function to send the mail
            subject = 'Message from  portfolio website'
            form_data = {
                'name':name,
                'email': email,
                'message': message
            }
            message = message = '''
            From:\n\t\t{}\n
            Email:\n\t\t{}\n
            Message:\n\t\t{}\n
            '''.format(form_data['name'], form_data['email'], form_data['message'])
            send_mail(
                subject,
                 message,
                 '',
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently = False,
            )
        # rendering the results on a template
        
            return render(request,'myapp/success.html')
    
        return render(request,'index.html')

# Create your views here.