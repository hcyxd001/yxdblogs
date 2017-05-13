from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.homepage),
    url(r'^post/(.*)/$',views.showpost),
    url(r'^mysql_url/$',views.mysql_url),
    url(r'^redis_url/$',views.redis_url),
    url(r'^python2_url/$',views.python2_url),
    url(r'^linux_url/$',views.linux_url),
    url(r'^mac_url/$',views.mac_url),
    url(r'^exploit_url/$',views.exploit_url),
    url(r'^mysql_content/(\d+)/$',views.mysql_content),
    #url(r'^redis_eaaay/(\d+)/$',views.reids_eaaay),
    #url(r'^python2_eaaay/(\d+)/$',views.python2_eaaay),
    #url(r'^linux_eaaay/(\d+)/$',views.linux_eaaay),
    #url(r'^max_eaaay/(\d+)/$',views.mac_eaaay),
    #url(r'^exploit_eaaay/(\d+)/$',views.exploit_eaaay),
    
]