from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'LoginProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^LoginApp/', include('LoginApp.urls',namespace='LoginApp')),
    url(r'^admin/', include(admin.site.urls)),
]
