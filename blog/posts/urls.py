from django.conf.urls import url
from . import views

app_name = 'posts'
urlpatterns = [
    url(r'^$', views.archive, name='archive')
]
