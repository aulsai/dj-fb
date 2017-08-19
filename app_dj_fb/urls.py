from django.conf.urls import patterns, include, url


from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proj_dj_fb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^', TestView.as_view()),    
)
