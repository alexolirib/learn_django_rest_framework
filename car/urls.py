from django.conf.urls import url
from car import views



urlpatterns = [
    # url(r'^student$', views.student_list),
    url(r'^$', views.CarListAndAdd.as_view()),
    url(r'^(?P<id_carro>[0-9]+)$', views.CarDetail.as_view()),
]