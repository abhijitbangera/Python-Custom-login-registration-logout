
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$','myauth.views.mylogin',name='login'),
    url(r'^register/$','myauth.views.register',name='register'),
    url(r'^logout/$','myauth.views.mylogout',name='logout'),
]
