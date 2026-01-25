from django.contrib import admin
from .models import Contacts, Callrequest, Pricerequest, Fquestions, Slider, Pages, TextBlock, ImageBlock, ImageTextBlock, VideoBlock
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

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("text_min", "id", "ranc", "show",)
    list_editable = ("ranc", "show",)

class TextBlockInline(admin.StackedInline):
    extra = 1
    model = TextBlock

class ImageBlockInline(admin.StackedInline):
    extra = 1
    model = ImageBlock

@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = ("title", "page",)
    inlines =(TextBlockInline, ImageBlockInline,)
