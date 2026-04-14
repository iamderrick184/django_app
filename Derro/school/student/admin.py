from django.contrib import admin
from student.models import Person
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display=['name','age','email']
admin.site.register(Person)
