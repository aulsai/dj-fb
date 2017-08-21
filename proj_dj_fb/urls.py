from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proj_dj_fb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),    
    url(r'^i18n/', include('django.conf.urls.i18n')),    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('app_dj_fb.urls')),
)

#urlpatterns += i18n_patterns('',    
#    
#)
