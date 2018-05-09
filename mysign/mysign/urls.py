"""mysign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from productdata import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prodata',views.productdata),
    path('getcharts/normalvol',views.getnormalvol),
    path('getcharts/abnormalvol',views.getabnormalvol),
    path('getcharts/abnormalcur',views.getabnormalcur),
    path('getcharts/abpf',views.getabnormalpowerfactor),
    path('getcharts/volbalance',views.getVolBalance),
    path('getcharts/abvolbalance',views.getabVolBalance),
    path('getcharts/curbalance',views.getCurBalance),
    path('getcharts/abcurbalance',views.getabCurBalance),
    path('getcharts/voldevia',views.getvoldevia),
    path('getcharts/normalcur',views.getnormalcur),
    path('getcharts/abcurvol',views.getabcurvol),
    path('getcharts/abcurvoldevia',views.getabcurvoldevia),
    path('getcharts/abcurvolbalance',views.getabcurVolBalance),
    path('getcharts/abvoldevia',views.getabvoldevia),
    path('getcharts/abvolcur',views.getabvolcur),
    path('getcharts/abvolcurbalance',views.getabVolCurBalance),
    path('getcharts/revol',views.getReverseVol),
    path('getcharts/revoldevia',views.getRevoldevia),
    path('getcharts/revolbalance',views.getReVolBalance),
    path('getcharts/recur',views.getRecur),
    path('getcharts/recurbalance',views.getReCurBalance),
    path('getcharts/pfvol',views.getPfVol),
    path('getcharts/pfvoldevia',views.getPfvoldevia),
    path('getcharts/pfvolbalance',views.getPfVolBalance),
    path('getcharts/pfcur',views.getPfcur),
    path('getcharts/pfcurbalance',views.getPfCurBalance),
    path('getcharts/norpf',views.getnopowerfactor),
    path('getcharts/avpf',views.getAvPowerFactor),
    path('getcharts/cvpf',views.getCvPowerFactor),
    path('getcharts/repf',views.getRePowerFactor)
]
