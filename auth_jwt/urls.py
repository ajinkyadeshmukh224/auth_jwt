from django.urls import path
from .views import CustomTokenObtainView

urlpatterns = [
    path('token/', CustomTokenObtainView.as_view(), name='token_obtain_pair'),
]
