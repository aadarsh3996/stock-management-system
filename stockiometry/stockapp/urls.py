from django.urls import path
from django.conf.urls import url,include
from stockapp import views
from stockapp.views import detailed,movement,buy,sell,forest,deep
import stockapp.views

app_name='stockapp'

urlpatterns=[

    url(r'^$',views.home,name='home'),
    url(r'^real/',views.home,name='real'),
    url(r'^detail/',detailed,name='detailed'),

    url(r'^movement/',movement,name='movement'),
    url(r'^forest/',forest,name='forest'),
    url(r'^deep_learning/',deep,name='deep'),

    url(r'^buy/',buy,name='buy'),
    url(r'^sell/',sell,name='sell'),
    url(r'^logout',views.user_logout,name='user_logout'),

    ]
