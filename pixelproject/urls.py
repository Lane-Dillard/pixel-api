from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from pixelapi.views import login_user, register_user
from pixelapi.views.profile import Profile  # Import the function directly

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'profile', Profile, 'profile')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user)
]