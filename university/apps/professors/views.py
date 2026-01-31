from django.shortcuts import render, get_object_or_404, redirect
from apps.courses.models import Course
from apps.students.models import Enrollment
# professors can see their courses
#
def my_teaching_courses(request):
    courses = Course.objects.filter(professor=request.user)
    return render(request, 'professors/my_courses.html', {'courses': courses})
