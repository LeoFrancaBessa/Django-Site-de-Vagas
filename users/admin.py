from django.contrib import admin
from . models import User, Applicant, Company

# Register your models here.
admin.site.register(User)
admin.site.register(Applicant)
admin.site.register(Company)