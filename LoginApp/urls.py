from django.conf.urls import include, url
from LoginApp import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register_success/', views.register_success, name='register_success'),
    url(r'^login_success/$', views.login_success, name='login_success'),     
    url(r'^register_form/$', views.register_form, name='register_form'),
    url(r'^register_success_form/', views.register_success_form, name='register_success_form'),
    #url(r'^login_form/$', views.login_form, name='login_form'),
     
]
