from django.urls import path, include
from rest_framework import routers

from Post.views import PostViewSet
router = routers.DefaultRouter()
router.register("post", PostViewSet)

urlpatterns = [
    path("", include(router.urls))
]
