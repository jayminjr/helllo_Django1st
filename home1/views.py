from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home1.models import Contact
from django.contrib import messages

# Create your views here.


def index(request):
    context = {
        "variable": "This is test varrrrrr",
    }
    return render(request, "index.html", context)
    # return HttpResponse("this is home page")


def about(request):
    return render(request, "about.html")
    # return HttpResponse("this is about page")


def services(request):
    return render(request, "services.html")
    # return HttpResponse("this is services page")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject,
                          message=message, date=datetime.now())
        contact.save()
        messages.success(request, 'Your message has been sent...!')

    return render(request, "contact.html")
    # return HttpResponse("this is contact page")
