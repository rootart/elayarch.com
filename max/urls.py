from django.conf.urls import patterns, include, url
from django.conf import settings

from portfolio.views import PortfolioItemFeed

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^imperavi/', include('imperavi.urls')),
    url(r'^feed/$', PortfolioItemFeed(), name='feed'),
    url(r'$^', 'portfolio.views.homepage', name='homepage'),
    url(r'^(?P<category_slug>[\w\s-]+)/$', 'portfolio.views.category', name='category'),
    url(r'^(?P<category_slug>[\w\s-]+)/(?P<slug>[\w\s-]+)', 'portfolio.views.item_details', name='details')

)

urlpatterns += patterns('',
    (r'^grappelli/', include('grappelli.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
