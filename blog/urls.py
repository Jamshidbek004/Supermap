from django.urls import path
from .views import index, bulutli_gis_serveri, ai_gis, cloud_gis, \
    onlinegisplatform, html_3d_gis, terminalgisforpc, gis_10_i, comp_gis_terminali, \
    edge_gis_server,  gis9, tabiiyofat, joinus, kattamalumot, mulkboshqarish, suvsaqlash, \
    transport, terminalgisformobile, aqllishahar, xavfsizlik, yermulk, \
    cross_platform, tabiatresurs
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('bulutli_gis_serveri/', bulutli_gis_serveri, name="bulutligisserveri"),
    path('ai_gis/', ai_gis, name="ai_gis"),
    path('asosiytexnalogiyalar/', asosiytexnalogiyalar, name="asosiytexnalogiyalar"),
    path('cloud_gis/', cloud_gis, name="cloud_gis"),
    path('onlinegisplatform/', onlinegisplatform, name="onlinegisplatform"),
    path('html_3d_gis/', html_3d_gis, name="html_3d_gis"),
    path('terminalgisforpc/', terminalgisforpc, name="terminalgisforpc"),
    path('gis_10_i/', gis_10_i, name="gis_10_i"),
    path('comp_gis_terminali/', comp_gis_terminali, name="terminalgisforweb"),
    path('edge_gis_server/', edge_gis_server, name="edge_gis_server"),
    path('joinus/', joinus, name="joinus"),
    path('events/', events, name="events"),
    path('terminalgisformobile/', terminalgisformobile, name="terminalgisformobile"),
    path('tabiiyofat/', tabiiyofat, name="tabiiyofat"),
    path('supermapgishaqida/', supermapgishaqida, name="supermapgishaqida"),
    path('gis9/', gis9, name="gis9"),
    path('news/', news, name="news"),
    path('tabiyresurs/', tabiatresurs, name="tabiiyresurs"),
    path('bimgis/', bimgis, name="bimgis"),
    path('mulkboshqarish/', mulkboshqarish, name="mulkboshqarish"),
    path('kattamalumot/', kattamalumot, name="kattamalumot"),
    path('suvsaqlash/', suvsaqlash, name="suvsaqlash"),
    path('transport/', transport, name="transport"),
    path('aqllishahar/', aqllishahar, name="aqllishahar"),
    path('xavfsizlik/', xavfsizlik, name="xavfsizlik"),
    path('yermulk/', yermulk, name="yermulk"),
    path('cross_platform/', cross_platform, name="cross_platform"),
    # path('yangilik/<int:id>', articlesdetel, name="yangilik"),
    # path('articles/', articles, name="articles"),
    path('detel/<int:id>', indexdetel, name="detel"),
    path('detel2/<int:id>', indexdetel2, name="detel2"),
    # path('edit/<int:pk>', Edit, name="edit"),
    # path('delet/<int:pk>', Delete, name="delet")


]