from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
# TODO подключите UserViewSet из Djoser.views к нашим urls.py
# TODO для этокого рекоммендуется использовать SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

user_router = SimpleRouter()
user_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(user_router.urls)),
    path("token/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
]
