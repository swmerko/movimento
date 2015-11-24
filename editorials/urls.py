from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _


urlpatterns = patterns(
    '',
    # url(r'^$', 'frontend_page.views.home', name='home'),
    # url(r'^home/$', 'frontend_page.views.home'),
    url(_(r'^events/map/$'), 'editorials.views.events_map', name='events_map'),
)
