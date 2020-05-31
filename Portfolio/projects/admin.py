from django.contrib import admin

# Register your models here.

from .models import Projects,Certifications,Contact


admin.site.register(Certifications)
admin.site.register(Contact)

@admin.register(Projects)
class BlogpostAdmin(admin.ModelAdmin):
    class Media:
        js = ('projects/tinyInject.js',)