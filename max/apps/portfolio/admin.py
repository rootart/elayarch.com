from django.contrib import admin


from portfolio.models import PortfolioItem, PortfolioItemCategory, ItemImage


admin.site.register(PortfolioItem)
admin.site.register(PortfolioItemCategory)
admin.site.register(ItemImage)
