from django.contrib import admin
from .models import Contacts, Callrequest, Pricerequest, Fquestions
# Register your models here.

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("title", "ranc", "show_in_top", "show_in_bottom",)
    list_editable = ("ranc", "show_in_top", "show_in_bottom",)

@admin.register(Callrequest)
class CallrequestAdmin(admin.ModelAdmin):
    list_display = ("number", "dateandtame",)

@admin.register(Pricerequest)
class PricerequestAdmin(admin.ModelAdmin):
    list_display = ("number", "qwestion",)

@admin.register(Fquestions)
class FquestionsAdmin(admin.ModelAdmin):
    list_display = ("question", "ranc", "show",)
    list_editable = ("ranc", "show",)