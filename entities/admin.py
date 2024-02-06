from django.contrib import admin

from .models import Brand, Entity, Category, Specification


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
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


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
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


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
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
