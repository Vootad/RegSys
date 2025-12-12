from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Lesson, TimeSlot
from .serializers import LessonSerializer, TimeSlotSerializer

# ------------------- API Views -------------------

# ویو‌ست برای مدیریت درس‌ها (CRUD کامل)
# فقط ادمین (مدیر آموزش) دسترسی دارد
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAdminUser]  # فقط کاربری که is_staff=True باشد

# ویو‌ست برای زمان‌بندی‌ها
class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
    permission_classes = [IsAdminUser]

# ------------------- Template Views (Frontend) -------------------

def login_page(request):
    """صفحه ورود"""
    return render(request, 'login.html')

def dashboard_page(request):
    """صفحه داشبورد مدیریت"""
    return render(request, 'dashboard.html')
