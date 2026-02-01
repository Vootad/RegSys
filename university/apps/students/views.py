from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from apps.courses.models import Course, SystemSetting
from .models import Enrollment

from django.shortcuts import redirect


def student_dashboard(request):
    return redirect('courses:dashboard')

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    student = request.user
    settings = SystemSetting.objects.first()
    max_val = settings.max_units if settings else 20

    if Enrollment.objects.filter(student=student, course=course).exists():
        messages.error(request, "این درس قبلاً در این ترم اخذ شده است.")
        return redirect('students:dashboard')


    if course.enrolled_students.count() >= course.capacity:
        messages.error(request, "ظرفیت این درس تکمیل شده است.")
        return redirect('students:dashboard')



@login_required
def drop_course(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id, student=request.user)
    enrollment.delete()
    messages.success(request, "واحد مورد نظر با موفقیت حذف شد.")
    return redirect('students:dashboard')


