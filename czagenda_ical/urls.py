from django.conf.urls.defaults import patterns,  url
from czagenda_ical.views import IcalView

urlpatterns = patterns('',
    (r'^(?P<pk>[^\.]+)\.(?P<format>ics|txt)$', IcalView.as_view(), {}, 'czagenda_event_ical'),
    
)
