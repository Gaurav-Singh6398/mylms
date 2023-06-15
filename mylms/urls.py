"""mylms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from library import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home),
    path('addrec',views.addrec),
    path('add',views.add),
    path('modify',views.modify),
    path('modrec',views.modrec),
    path('mod',views.mod),
    path('m1',views.m1),
    path('mod1',views.mod1),
    path('m2',views.m2),
    path('mod2',views.mod2),
    path('m3',views.m3),
    path('mod3',views.mod3),
    path('m4',views.m4),
    path('mod4',views.mod4),
    path('m5',views.m5),
    path('mod5',views.mod5),
    path('delrec',views.delrec),
    path('delete',views.delete),
    path('searchrec',views.searchrec),
    path('s1',views.s1),
    path('s2',views.s2),
    path('s3',views.s3),
    path('search1',views.search1),
    path('search2',views.search2),
    path('search3',views.search3),
    path('caddrec',views.caddrec),
    path('cadd',views.cadd),
    path('cmodrec',views.cmodrec),
    path('cmod',views.cmod),
    path('issue',views.issue),
    path('iss',views.iss),
    path('returnb',views.returnb),
    path('ret',views.ret),
    path('defaulter',views.defaulter),
]
