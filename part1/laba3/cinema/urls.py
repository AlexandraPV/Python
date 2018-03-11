from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'^delete/$', views.delete),
    url(r'^update/$', views.update),
    url(r'^add/$', views.add),
    url(r'^post_form_add/$', views.post_form_add),
    url(r'^search_city/$', views.search_city),
    url(r'^search_seance/$', views.search_seance),
    url(r'^post_form_update/$', views.post_form_update),
    url(r'^kp_3/$', views.kp),
    # url(r'^post_form_search_bm/$', views.post_form_search_bm),
    url(r'^search/$', views.search),
    url(r'^search_bm/$', views.search_bm),
]
