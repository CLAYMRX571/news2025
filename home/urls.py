from django.urls import path
from .views import UserRegistrationView, UserLoginView, LogoutView, UserUpdateView, PasswordResetView

app_name = "home"
urlpatterns = [
    path("sign-up/", UserRegistrationView.as_view(), name="signup"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("update/", UserUpdateView.as_view(), name="userupdate"),
    path("reset/", PasswordResetView.as_view(), name="reset"),
]
