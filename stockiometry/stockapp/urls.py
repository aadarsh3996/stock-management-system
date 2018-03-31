from django.urls import path
from django.conf.urls import url,include
from stockapp import views
from stockapp.views import detailed,movement

app_name='stockapp'

urlpatterns=[

    url(r'^$',views.home,name='home'),
    url(r'^real/',views.home,name='real'),

    url(r'^detail/',detailed,name='detailed'),
    url(r'^movement/',movement,name='movement')

    ]
