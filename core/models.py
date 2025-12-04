from django.db import models
from django.contrib.auth.models import AbstractUser

# ۱. مدل User سفارشی
class User(AbstractUser):
    """
    مدل کاربر برای سیستم دانشگاه
    دارای سه نقش: admin, student, professor
    """
    class Role(models.TextChoices):
        ADMIN = 'admin', 'مدیر'
        STUDENT = 'student', 'دانشجو'
        PROFESSOR = 'professor', 'استاد'
    
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
        verbose_name='نقش'
    )
    
    student_id = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True,
        verbose_name='شماره دانشجویی'
    )
    
    professor_code = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True,
        verbose_name='کد استادی'
    )
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

# ۲. مدل Course (درس)
class Course(models.Model):
    """
    مدل درس‌های دانشگاه
    """
    name = models.CharField(max_length=200, verbose_name='نام درس')
    code = models.CharField(max_length=20, unique=True, verbose_name='کد درس')
    capacity = models.IntegerField(verbose_name='ظرفیت')
    professor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': User.Role.PROFESSOR},
        verbose_name='استاد'
    )
    time = models.CharField(max_length=100, verbose_name='زمان برگزاری')
    location = models.CharField(max_length=100, verbose_name='مکان')
    
    def __str__(self):
        return f"{self.name} ({self.code})"
    
    class Meta:
        verbose_name = 'درس'
        verbose_name_plural = 'درس‌ها'

# ۳. مدل Enrollment (ثبت‌نام)
class Enrollment(models.Model):
    """
    مدل ثبت‌نام دانشجو در درس
    """
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': User.Role.STUDENT},
        verbose_name='دانشجو'
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='درس')
    enrollment_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت‌نام')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    
    class Meta:
        unique_together = ['student', 'course']  # هر دانشجو فقط یک بار در هر درس
        verbose_name = 'ثبت‌نام'
        verbose_name_plural = 'ثبت‌نام‌ها'
    
    def __str__(self):
        return f"{self.student.username} در {self.course.name}"