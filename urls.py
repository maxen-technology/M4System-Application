from django.conf.urls import include, url
from django.contrib import admin
# We load them here to override their template.
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from webview.views import settings
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url='/public/img/favicon.ico')),  # serve the favicon and avoid 404s
    url(r'^', include('webview.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),  # add admin
    url(r'^login/', login, {'template_name': 'login.html'}, name='login'), # override the template with ours
    url(r'^logout/', logout, {'template_name': 'loggedout.html'}, name='logout'), # override the template with ours
    url(r'^password_reset/', password_reset, {'template_name': 'lostpass.html'}, name='password_reset'), # override the template with ours
    url(r'^password_reset_done/', password_reset_done, {'template_name': 'resetdone.html'}, name='password_reset_done'), # override the template with ours
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, {'template_name': 'resetconfirm.html', 'post_reset_redirect': '/'}, name='password_reset_confirm'), # override the template with ours
    url(r'^password_reset_complete/', password_reset_complete, name='password_reset_complete'), # override the template with ours
    url(r'^settings/', settings, name='settings'),
    # url(r'^500/$', 'django.views.defaults.server_error'),
]