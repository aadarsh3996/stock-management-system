from django.urls import path
from django.conf.urls import url,include
from account import views

app_name='account'

urlpatterns = [

    url(r'^login/$',views.user_login,name='user_login'),
    url(r'^register/',views.user_register,name='register'),
    url(r'^index/$',views.index,name='index'),
    url(r'^home/',include('stockapp.urls',namespace='stockapp'),name='home')



]
