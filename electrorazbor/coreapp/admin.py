from django.contrib import admin
from .models import Contacts, Callrequest
# Register your models here.

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("title", "ranc", "show_in_top", "show_in_bottom",)
    list_editable = ("ranc", "show_in_top", "show_in_bottom",)

@admin.register(Callrequest)
class CallrequestAdmin(admin.ModelAdmin):
    list_display = ("number", "dateandtame",)