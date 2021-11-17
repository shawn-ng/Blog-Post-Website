from django.urls import path, include
from rest_framework import routers

from .views import SearchUserView

router = routers.DefaultRouter()
router.register('userSearch', SearchUserView)

urlpatterns = router.urls
