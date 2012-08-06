from django.shortcuts import render, get_object_or_404
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from portfolio.models import PortfolioItemCategory, PortfolioItem, ItemImage


def homepage(request):
    data = {
        'items': PortfolioItem.objects.filter(is_published=True),
    }
    return render(request, 'index.html', data)


def category(request, category_slug):
    category = get_object_or_404(PortfolioItemCategory, slug=category_slug)
    items = category.portfolioitem_set.all()
    data = {
        'category': category,
        'items': items
    }
    return render(request, 'category.html', data)


def item_details(request, category_slug, slug):
    category = get_object_or_404(PortfolioItemCategory, slug=category_slug)
    item = PortfolioItem.objects.get(category=category, slug=slug)
    images = ItemImage.objects.filter(portfolioitem=item)
    data = {
        'item': item,
        'category': category,
        'images': images
    }
    return render(request, 'details.html', data)


class PortfolioItemFeed(Feed):
    title = ""
    link = ""
    description = ""

    def items(self):
        return PortfolioItem.objects.order_by('-created')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse('details', args=[item.category.slug, item.slug])
