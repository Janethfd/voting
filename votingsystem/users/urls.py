from django.urls import path
from .views import sign_up, login, password_reset


urlpatterns = [
    path('signup/', sign_up, name="signup"),
    path('login/', login, name='login'),
    path('password_reset/', password_reset, name="password-reset")

]
