from django.shortcuts import render, get_object_or_404, redirect
from apps.courses.models import Course
from apps.students.models import Enrollment
# professors can see their courses
#
def my_teaching_courses(request):
    courses = Course.objects.filter(professor=request.user)
    return render(request, 'professors/my_courses.html', {'courses': courses})

def enrolled_students(request, course_id):
    course = get_object_or_404(Course, id=course_id, professor=request.user)
    enrollments = Enrollment.objects.filter(course=course, term="1402-2").order_by('student__last_name')
    return render(request, 'professors/students.html', {'enrollments': enrollments, 'course': course})
