from django.db import models


class PortfolioItemCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Item category'
        verbose_name_plural = 'Item categories'
        ordering = ('-position',)

    def __unicode__(self):
        return self.title

    @property
    def items(self):
        return self.portfolioitem_set.filter(is_published=True).count()


class PortfolioItem(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    category = models.ForeignKey(PortfolioItemCategory)
    top_image = models.ImageField(upload_to='portfolio/images/top')
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pub_date = models.DateField(blank=True, null=True)
    position = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-position',)


class ItemImage(models.Model):
    portfolioitem = models.ForeignKey(PortfolioItem)
    descrption = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="portfolio/images")
    position = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.portfolioitem.title

    class Meta:
        verbose_name = 'Item image'
        verbose_name_plural = 'Item images'
        ordering = ('-position',)
