from django.contrib import admin
from . models import User, Applicant, Company

# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(User, UsersAdmin)
admin.site.register(Applicant)
admin.site.register(Company)