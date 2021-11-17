from django.urls import path, include
from rest_framework import routers

from .views import AllUserPostView

router = routers.DefaultRouter()
router.register("allUserPost", AllUserPostView)
urlpatterns = [
    path("", include(router.urls))
]
