

from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.home, name = 'blog_home'),
    url(r'^content/(?P<article_id>\d+)$', views.content, name = 'blog_content'),
    url(r'^edit/(?P<article_id>\d+)$', views.edit, name = 'edit_page'),
    url(r'^edit/action$', views.form_action, name = 'edit_action')
]