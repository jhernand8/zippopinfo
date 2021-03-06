from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import census.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', census.views.index, name='index'),
    url(r'^db', census.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^addZip$', census.views.add_zip, name='zips'),
]
