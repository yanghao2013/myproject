from django.contrib import admin

# Register your models here.
from .models import AssociatedItem
class ItemInlineAdmin(admin.StackedInline):
    model = AssociatedItem