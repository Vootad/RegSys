from rest_framework import serializers
from .models import User, Course, Enrollment

# ۱. سریالایزر کاربر
class UserSerializer(serializers.ModelSerializer):
    """
    تبدیل مدل User به JSON برای API
    """
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'full_name',
            'role', 'student_id', 'professor_code',
            'first_name', 'last_name', 'is_active'
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'password': {'write_only': True}  # رمز در JSON نشان داده نمی‌شود
        }
    
    def get_full_name(self, obj):
        """دریافت نام کامل کاربر"""
        return f"{obj.first_name} {obj.last_name}".strip()
    
    def create(self, validated_data):
        """ایجاد کاربر جدید با رمز عبور هش‌شده"""
        user = User.objects.create_user(**validated_data)
        return user

# ۲. سریالایزر درس
class CourseSerializer(serializers.ModelSerializer):
    """
    تبدیل مدل Course به JSON برای API
    """
    professor_name = serializers.CharField(source='professor.get_full_name', read_only=True)
    enrolled_count = serializers.SerializerMethodField()
    available_seats = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = [
            'id', 'name', 'code', 'capacity',
            'professor', 'professor_name',
            'time', 'location',
            'enrolled_count', 'available_seats'
        ]
        read_only_fields = ['id', 'enrolled_count', 'available_seats']
    
    def get_enrolled_count(self, obj):
        """تعداد دانشجویان ثبت‌نام کرده در این درس"""
        return obj.enrollment_set.filter(is_active=True).count()
    
    def get_available_seats(self, obj):
        """تعداد صندلی‌های خالی"""
        enrolled = obj.enrollment_set.filter(is_active=True).count()
        return obj.capacity - enrolled

# ۳. سریالایزر ثبت‌نام
class EnrollmentSerializer(serializers.ModelSerializer):
    """
    تبدیل مدل Enrollment به JSON برای API
    """
    student_name = serializers.CharField(source='student.get_full_name', read_only=True)
    course_name = serializers.CharField(source='course.name', read_only=True)
    course_code = serializers.CharField(source='course.code', read_only=True)
    
    class Meta:
        model = Enrollment
        fields = [
            'id', 'student', 'student_name',
            'course', 'course_name', 'course_code',
            'enrollment_date', 'is_active'
        ]
        read_only_fields = ['id', 'enrollment_date']