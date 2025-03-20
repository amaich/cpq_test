from django.contrib import admin
from .models import Product, Item, Resource, Attribute, Condition, ConditionItem

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    pass


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    pass


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    pass


@admin.register(ConditionItem)
class ConditionItemAdmin(admin.ModelAdmin):
    pass