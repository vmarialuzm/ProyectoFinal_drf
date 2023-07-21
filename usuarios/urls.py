from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from usuarios import views

usuarios_router = routers.DefaultRouter(trailing_slash=False)
usuarios_router.register('', views.GetUsers, basename="listar-usuarios")

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("jwt/create/", jwt_views.TokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", jwt_views.TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", jwt_views.TokenVerifyView.as_view(), name="jwt-verify"),
]

urlpatterns += usuarios_router.urls