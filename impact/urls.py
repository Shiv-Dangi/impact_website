from django.conf.urls import patterns, url
from django.conf import settings
from impact import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^impact/header/$', views.header_info, name='header_info'),
    url(r'^impact/footer/$', views.footer_info, name='footer_info'),
    url(r'^impact/aboutus/$', views.aboutus_info, name='aboutus_info'),
    url(r'^impact/service/$', views.service_info, name='service_info'),
    url(r'^impact/advertisement/$', views.advertisement_info, name='advertisement_info'),
    url(r'^impact/gallery/$', views.gallery_info, name='gallery_info'),
    url(r'^impact/events/$', views.events_info, name='events_info'),
    url(r'^impact/jobs/$', views.jobs_info, name='jobs_info'),
    url(r'^impact/contactus/$', views.contactus_info, name='contactus_info'),
    
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)
