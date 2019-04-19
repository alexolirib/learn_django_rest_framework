from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from student import views



urlpatterns = [
    # url(r'^student$', views.student_list),
    url(r'^$', views.StudentList.as_view()),
    url(r'^(?P<pk>[0-9]+)$', views.StudentDetail.as_view()),
    url(r'^customized$', views.StudentCustomized.as_view())
]


