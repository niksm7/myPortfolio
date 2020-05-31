from django.shortcuts import render,HttpResponse
from .models import Projects,Certifications
from django.contrib import messages

# Create your views here.

def projectsHome(request):

    allProds = []
    catprod = Projects.objects.values('project_category','project_id')
    allProds.append(Projects.objects.filter(project_category = "Django"))
    
    cats = {item['project_category'] for item in catprod if item['project_category']!="Django"}
    for cat in cats:
        prod = Projects.objects.filter(project_category=cat)
        allProds.append(prod)
    params = {'allProds':allProds}
    return render(request,'projects/projects.html',params)

def projectView(request,id):
    project = Projects.objects.filter(project_id=id)[0]
    return render(request,'projects/projectView.html',{'project':project})

def certifications(request):
    all_certi =  Certifications.objects.all()
    x = [i.preference for i in all_certi]
    x.sort()
    all_certi1 = []
    for i in x:
        for j in all_certi:
            if j.preference==i:
                all_certi1.append(j)
    return render(request,'projects/certifications.html',{'all_certi':all_certi1})