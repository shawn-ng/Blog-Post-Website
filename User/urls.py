from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .api import RegisterApi
from .views import UserViewSet

# router = routers.DefaultRouter()
# router.register("viewuser", UserViewSet)
urlpatterns = [
    path('api/register', RegisterApi.as_view()),
    # path('', router.urls)
]
