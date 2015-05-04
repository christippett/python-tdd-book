from django.conf.urls import patterns, include, url
from django.contrib import admin
from lists import urls as list_urls
from accounts import urls as account_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'superlists.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^lists/', include('lists.urls')),
    url(r'^accounts/', include(account_urls)),
    # url(r'^admin/', include(admin.site.urls)),
)
