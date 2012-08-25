from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from imperavi.admin import ImperaviAdmin
from portfolio.models import PortfolioItem, PortfolioItemCategory, ItemImage
from django.contrib.flatpages.models import FlatPage




class ItemImageAdmin(AdminImageMixin, admin.TabularInline):
    model = ItemImage


class PortfolioItemAdmin(ImperaviAdmin):
    inlines = [ItemImageAdmin, ]
    list_display = ('__unicode__', 'is_published', 'position')


class PortfolioItemCategoryAdmin(ImperaviAdmin):
    list_display = ('__unicode__', 'position')

admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(PortfolioItemCategory, PortfolioItemCategoryAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, ImperaviAdmin)
