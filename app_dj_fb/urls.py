from django.conf.urls import patterns, include, url


from .views import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proj_dj_fb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/user/create/', views.FBUserCreate),    
    url(r'^', views.TestView.as_view()),     
)
