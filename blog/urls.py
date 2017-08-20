from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^teste/', views.teste),
    url(r'^menu/', views.menu),
    url(r'^credts/', views.credts),
    url(r'^projects/', views.projects),
]
