from django.conf.urls import include, url
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path
from HouseMgt_API.urls import router


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace="oauth2_provider")),
]
