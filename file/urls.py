from . import views
import local_settings
from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = "file"

router = DefaultRouter()

if not settings.DEBUG:
    router.include_root_view = False

# router.register("", views.UsersViewSet)
urlpatterns = [

    path('', include(router.urls)),
]
