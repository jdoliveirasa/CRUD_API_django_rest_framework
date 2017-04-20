#from django.conf.urls import patterns, include, url
from django.conf.urls import include, url 
#from django.conf.urls.i18n import i18n_patterns

from django.contrib import admin
admin.autodiscover()

#urlpatterns = patterns(
#urlpatterns = i18n_patterns([
urlpatterns = (
    #'',
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
#)