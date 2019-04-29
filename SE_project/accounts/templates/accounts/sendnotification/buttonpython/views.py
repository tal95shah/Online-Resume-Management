from django.shortcuts import render
import requests
import smtplib


def button(request):

    return render(request,'admin1.html')

def output(request):

	content: 'Hi Dear ! please download your data as soon as possible.It will be deleted automatically in after given dead line.
	Best Regards,
	Admin ORMS'
	mail=smtplib.SMTP('smtp.gmail.com',567)
	mail.echo()
	mail.starttls()
	mail.login('email','password')
	mail.sendmail('fromemail','receiver',content)
	mail.close()

    
    return render(request,'home.html')