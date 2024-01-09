from django.contrib import admin
from core.models import Contact

# Register your models here.
@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'f_name', 'l_name', 'email', 'phone_number', 'message']
