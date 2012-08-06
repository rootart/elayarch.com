from portfolio.models import PortfolioItemCategory


def categories(request):
    return {
        'CATEGORIES': PortfolioItemCategory.objects.all()
    }
