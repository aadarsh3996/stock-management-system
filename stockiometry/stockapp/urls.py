from django.urls import path
from django.conf.urls import url,include
from stockapp import views

app_name='stockapp'

urlpatterns=[

    url(r'^',views.home,name='home'),

    ]
