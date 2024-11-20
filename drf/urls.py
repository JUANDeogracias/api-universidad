# drf/urls.py
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

APPEND_SLASH = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('docs/', include_docs_urls(title='API Documentation')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', lambda request: redirect('api/v1/')),
]
