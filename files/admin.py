from django.contrib import admin
from .models import Image, Video


# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
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
    # ordering = ("",)admin.register("Entity")


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
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
