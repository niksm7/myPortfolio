from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MinLengthValidator

class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)
    project_category = models.CharField(max_length=100,default="")
    main_image = models.ImageField(upload_to="projects/",default="")
    main_about = models.TextField(default='',validators=[MinLengthValidator(150)])
    git_link = models.CharField(max_length=500,default="")
    proj_video = models.FileField(_("Video"),upload_to="projects/",null=True,blank=True,default="")
    is_muted = models.BooleanField(_("If video has sound uncheck this"),default=True)
    content = models.TextField(default="")

    def __str__(self):
        return self.project_name


class Certifications(models.Model):
    preference = models.IntegerField(default=100)
    certi_id = models.AutoField(primary_key=True)
    certi_name = models.CharField(max_length=500)
    org = models.CharField(max_length=50)
    issue_date = models.DateField()
    cred_id = models.CharField(max_length=50,blank=True)
    cred_url = models.CharField(max_length=2000,blank=True)

    def __str__(self):
        return self.certi_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70,default="")
    msg = models.TextField(max_length=500,default="")

    def __str__(self):
        return self.name


    