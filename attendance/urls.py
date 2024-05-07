from django.urls import path
from .views import LoginTokenObtainPairView

urlpatterns = [
    path("login/", LoginTokenObtainPairView.as_view(), name="token_obtain_pair"),
]
