from blog import views
from django.conf.urls import url
urlpatterns = [
    url(r'article/(\d{4}/(\d{2}))',views.article_year),
    url(r'article/(?P<month>\d{4})',views.article_month),
    url(r'register',views.register),
    url(r'login', views.login)
]
