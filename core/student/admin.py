from django.contrib import admin
from .models import Student

admin.site.site_header = "Student Search PClub IITK Admin"
admin.site.site_title = "Student Search PClub IITK Admin Portal"
admin.site.index_title = "Welcome to Student Search PClub IITK Certificate Portal"

# Register your models here.
admin.site.register(Student)