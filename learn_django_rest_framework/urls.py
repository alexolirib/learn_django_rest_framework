from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^student/', include('student.urls')),
    url(r'^car/', include('car.urls')),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]