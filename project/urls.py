from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from welcome.views import index, health, post_list, post_detail, post_new, post_edit

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', post_list, name='post_list'),
    url(r'^health$', health),
    url(r'^admin/', admin.site.urls),
    url(r'^home$', post_list, name='post_list'),
    url(r'^home/post/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
    url(r'^post/new/', post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', post_edit, name='post_edit'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
