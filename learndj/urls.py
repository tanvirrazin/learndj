from django.conf.urls import patterns, include, url
from article.views import HelloTemplate

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learndj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', 'article.views.hello'),
    url(r'^hello_template/', 'article.views.hello_template'),
    url(r'^hello_template_simple/', 'article.views.hello_template_simple'),
    url(r'^hello_class_view/', HelloTemplate.as_view()),
    url(r'^articles/',include('article.urls')),
)
