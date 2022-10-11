
from django.contrib import admin
from django.urls import path, include

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
from cms.views import PageViewSet
router = routers.DefaultRouter()
router.register(r'pages', PageViewSet)

from cms.models import Page

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]



