from django.urls import path
from django.contrib import admin
from webapp import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
# from rest_framework_simplejwt import views as jwt_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', views.employeeList.as_view(), name='employee list'),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/jwt-communication/', views.TakeJWTPayload.as_view()),
]
