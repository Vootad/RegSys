from django.apps import AppConfig

class CoursesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.courses'  # ← این مسیر باید دقیقاً با مسیر اپ تو هماهنگ باشه
