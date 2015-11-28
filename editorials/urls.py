from django.conf.urls import patterns, url, include
from django.utils.translation import ugettext_lazy as _
from rest_framework.routers import DefaultRouter
from .rest import EventViewSet

urlpatterns = patterns(
    '',
    # url(r'^$', 'frontend_page.views.home', name='home'),
    # url(r'^home/$', 'frontend_page.views.home'),
    url(_(r'^events/map/$'), 'editorials.views.events_map', name='events_map'),
)

# api
router = DefaultRouter('skills')
router.register(r'events', EventViewSet, base_name='api_events')

urlpatterns += [
    url(r'^api/', include(router.urls)),
]