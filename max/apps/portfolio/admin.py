from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin

from portfolio.models import PortfolioItem, PortfolioItemCategory, ItemImage


class ItemImageAdmin(AdminImageMixin, admin.TabularInline):
    model = ItemImage


class PortfolioItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageAdmin, ]
    list_display = ('__unicode__', 'is_published', 'position')


class PortfolioItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'position')

admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(PortfolioItemCategory, PortfolioItemCategoryAdmin)
