from django.db import models
from apps.accounts.models import User

class Course(models.Model):
    # تعریف لیست کشویی برای روزهای هفته
    DAYS_OF_WEEK = [
        ('1', 'شنبه'),
        ('2', 'یکشنبه'),
        ('3', 'دوشنبه'),
        ('4', 'سه‌شنبه'),
        ('5', 'چهارشنبه'),
        ('6', 'پنج‌شنبه'),
        ('7', 'جمعه'),
    ]

    name = models.CharField(max_length=100, verbose_name="نام درس")
    code = models.CharField(max_length=20, unique=True, verbose_name="کد درس")
    capacity = models.IntegerField(verbose_name="ظرفیت")
    professor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        limit_choices_to={'is_professor': True}, 
        verbose_name="استاد"
    )
    # تغییر فیلد روز به انتخاب‌گر (Dropdown)
    day = models.CharField(
        max_length=1, 
        choices=DAYS_OF_WEEK, 
        default='1', 
        verbose_name="روز برگزاری"
    )
    start_time = models.TimeField(verbose_name="زمان شروع")
    end_time = models.TimeField(verbose_name="زمان پایان")
    location = models.CharField(max_length=100, verbose_name="مکان برگزاری")