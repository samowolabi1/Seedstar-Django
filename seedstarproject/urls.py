from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    url(r'^$', include('emailrecords.url')),
    path('admin/', admin.site.urls),
    path('emailrecords/', include('emailrecords.url')),
    path('list/', include('emailrecords.url'))
]
