from django.db import models
from accounts.models import Professor

# مدل زمان‌بندی (برای مدیریت روز و ساعت کلاس‌ها)
class TimeSlot(models.Model):
    DAYS_OF_WEEK = (
        ('shanbe', 'شنبه'),
        ('yekshanbe', 'یکشنبه'),
        ('doshanbe', 'دوشنبه'),
        ('seshanbe', 'سه‌شنبه'),
        ('chaharshanbe', 'چهارشنبه'),
        ('panjshanbe', 'پنج‌شنبه'),
        ('jome', 'جمعه'),
    )
    
    day = models.CharField(max_length=20, choices=DAYS_OF_WEEK, verbose_name="روز هفته")
    start_time = models.TimeField(verbose_name="ساعت شروع")
    end_time = models.TimeField(verbose_name="ساعت پایان")

    def __str__(self):
        return f"{self.get_day_display()} - {self.start_time} تا {self.end_time}"

# مدل درس
class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان درس")
    unique_code = models.CharField(max_length=20, unique=True, verbose_name="کد درس")
    capacity = models.PositiveIntegerField(verbose_name="ظرفیت")
    # ارتباط چند به چند: یک درس می‌تواند چندین زمان داشته باشد
    time_slots = models.ManyToManyField(TimeSlot, verbose_name="زمان‌های برگزاری")

    # professor = models.ForeignKey(
    #     Professor,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name="lessons"
    # )


    def __str__(self):
        return self.title
