from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    # detail
    url(r'^(\d+)/$', views.detail, name='detail')
]
