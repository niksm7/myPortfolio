from django.shortcuts import render
from projects.models import Contact
from django.http import HttpResponseRedirect

def index(request):
    return render(request,'index.html')


def contact(request):
    if request.method=="POST":
        name = request.POST.get('Name','')
        email = request.POST.get('Email','')
        msg = request.POST.get('Message','')
        contact = Contact(name=name,email=email,msg=msg)
        contact.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

    return HttpResponseRedirect('/')