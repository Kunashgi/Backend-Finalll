from django.conf.urls import url
from Data import views
from django.conf.urls.static import static

urlpatterns = [
  url(r'^reserva$', views.reservaApi),
  url(r'^reserva/([0-9]+)$', views.reservaApi),

  url(r'^users$', views.usersApi),
  url(r'^users/([0-9]+)$', views.usersApi),

  url(r'^cancelacion$', views.cancelacionApi),
  url(r'^cancelacion/([0-9]+)$', views.cancelacionApi),

  url(r'^contact$', views.contactApi),
  url(r'^contact/([0-9]+)$', views.contactApi),
  
]