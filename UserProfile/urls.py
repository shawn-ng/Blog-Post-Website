from django.urls import path, include
from rest_framework import routers, urlpatterns

from .views import UserProfileViewSet


router = routers.DefaultRouter()
router.register("userProfile", UserProfileViewSet)

urlpatterns = [
    path("", include(router.urls))
]
