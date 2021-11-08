from django.urls import path, include
from rest_framework import routers

from Friend.views import FriendViewSet

router = routers.DefaultRouter()
router.register('friend', FriendViewSet)

urlpatterns = [
    path('', include(router.urls))
]
