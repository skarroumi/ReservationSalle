from django.conf.urls import url
from . import views

urlpatterns = [
 url(r'^$', views.index, name='index'),



 url(r'^logout/$', views.logout_view, name='logout'),


 url(r'^register/$', views.register_view, name='register'),      # loads the FORM.HTML


 url(r'^history/$', views.history, name='history'),

 url(r'^dashboard/$', views.home_prof, name='home_prof'),
 url(r'^reservation/$', views.reservation, name='reservation'),
 url(r'^profil/$', views.profil, name='profil'),
 url(r'^reservation/supprimer_reservation/([0-9]+)/$', views.supprimer_reservation, name='supprimer_reservation'),
 ]