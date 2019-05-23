from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

# Create your models here.
class SubmitAttendance(models.Model):
    
    class Meta:
        db_table = 'attendance'
    
    PLACES = (
        ('TN', 'TANKS'),
        ('RT', 'Red Tails'),
        ('AN', 'ANNIE HALL'),
        ('NK', 'NOKUROXY'),
        ('HC', '七'),
        ('AM', 'ART MON ZEN'),
    )
    IN_OUT = (
        (1, 'IN'),
        (0, 'OUT'),
    )

    staff = models.ForeignKey(get_user_model(), verbose_name="スタッフ", on_delete=models.CASCADE, default=None)
    place = models.CharField(verbose_name='出勤場所名', max_length=50, choices=PLACES, default=None)
    in_out = models.IntegerField(verbose_name='IN/OUT', choices=IN_OUT, default=None)
    time = models.DateTimeField(verbose_name="打刻時間")

