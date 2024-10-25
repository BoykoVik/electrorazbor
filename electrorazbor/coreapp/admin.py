from django.contrib import admin
from .models import Contacts
# Register your models here.

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("title", "ranc", "show_in_top", "show_in_bottom",)
    list_editable = ("ranc", "show_in_top", "show_in_bottom",)