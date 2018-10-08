from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url


urlpatterns = [
    # Examples:
    # url(r'^$', 'buscoayuda4101.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('buscoayuda.urls', namespace="principal")),
    path('admin/', admin.site.urls),
]