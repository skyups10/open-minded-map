from django.contrib import admin
from .models import Institution

class InstitutionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Institution, InstitutionAdmin)