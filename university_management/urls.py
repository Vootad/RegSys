from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from main import views

# روتر برای ساخت خودکار URLهای API
router = DefaultRouter()
router.register(r'lessons', views.LessonViewSet)
router.register(r'timeslots', views.TimeSlotViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # اندپوینت‌های API
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # دریافت توکن
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # صفحات HTML
    path('', views.login_page, name='login'),
    path('dashboard/', views.dashboard_page, name='dashboard'),
]
