from django.urls import path
from . import views

urlpatterns = [
    path("",views.projectsHome,name="projectsHome"),
    path("certifications/",views.certifications,name="certifications"),
    path("projectView/<int:id>",views.projectView,name="projectsView"),

]