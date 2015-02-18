from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bluber.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # '?' is RegEx "operator" meaning the previous character
    # is optional.
    url(r'^homes?/?', 'bluber.views.home_view'),

    url(r'^admin/', include(admin.site.urls)),
)
