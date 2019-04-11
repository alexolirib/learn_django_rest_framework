from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from student import views
urlpatterns = [
    url(r'^student/$', views.student_list),
    url(r'^student2/$', views.StudentList.as_view()),
    url(r'^student/(?P<pk>[0-9])/$', views.student_detail),
    url(r'^student/customized/$', views.student_customized)
]


urlpatterns = format_suffix_patterns(urlpatterns)