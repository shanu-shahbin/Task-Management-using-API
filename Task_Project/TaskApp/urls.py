from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from . import views

urlpatterns = [
    # Task-related views
    path('tasks/', views.TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    
    # User registration and authentication
    path('auth/register/', views.RegisterUser.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
