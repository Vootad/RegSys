from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from apps.courses.models import Course, SystemSetting
from .models import Enrollment

from django.shortcuts import redirect


def student_dashboard(request):
    return redirect('courses:dashboard')