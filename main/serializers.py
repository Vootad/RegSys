from rest_framework import serializers
from .models import Lesson, TimeSlot

class TimeSlotSerializer(serializers.ModelSerializer):
    day_display = serializers.CharField(source='get_day_display', read_only=True)

    class Meta:
        model = TimeSlot
        fields = ['id', 'day', 'day_display', 'start_time', 'end_time']

class LessonSerializer(serializers.ModelSerializer):
    # نمایش کامل زمان‌ها به صورت تو در تو برای خواندن
    time_slots_details = TimeSlotSerializer(source='time_slots', many=True, read_only=True)
    # برای نوشتن (Create/Update)، فقط آی‌دی زمان‌ها را می‌گیریم
    time_slots = serializers.PrimaryKeyRelatedField(queryset=TimeSlot.objects.all(), many=True)

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'unique_code', 'capacity', 'time_slots', 'time_slots_details']
