from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import Registration, UserData

urlpatterns = [
    path('register/', Registration.as_view(), name='registration'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh_token'),
    path('user/', UserData.as_view(), name='user_data'),
]
