from django.conf.urls import url
from . import views
from django.contrib.auth.views import login , logout
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$',login, {'template_name':'form/login.html'}),
    url(r'^logout/$',logout, {'template_name':'form/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^register_fail/$' , views.reg_fail , name='reg_fail'),

    url(r'^api/$',views.UserList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$',views.UserList.as_view()),

]
