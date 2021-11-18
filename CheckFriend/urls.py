from django.urls import path, include
from rest_framework import routers

from .views import CheckFriendViewSet, CheckFriendStatusViewSet, CheckPendingFriendViewSet

router = routers.DefaultRouter()
router.register("checkFriend", CheckFriendViewSet)
router.register("friendStatus", CheckFriendStatusViewSet)
router.register("pendingFriend", CheckPendingFriendViewSet)

urlpatterns = [
    path('', include(router.urls))
]
