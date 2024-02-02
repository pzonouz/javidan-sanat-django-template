from django.contrib import admin
from .models import Customer


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass
    # list_display = ("",)
    # list_filter = ("",)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ("",)
    # readonly_fields = ("",)
    # search_fields = ("",)
    # date_hierarchy = ""
    # ordering = ("",)
