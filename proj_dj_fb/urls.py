from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proj_dj_fb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^', include('app_dj_fb.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
