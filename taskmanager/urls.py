from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


api_urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
]


urlpatterns = [
    path('', include('tasks.urls')),
    # Регистрация в сервисе
    path('api/v1/', include(api_urlpatterns), name='register'),
    # Получение, обновление токенов
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
