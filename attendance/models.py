from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

# Create your models here.
class Place(models.Model):
    # place model  
    class Meta:
        db_table = 'place'
    place = models.CharField(verbose_name='出勤場所名', max_length=50)

class Staff(models.Model):
    # logging in user model
    class Meta:
        db_table = 'staff'
    staff = models.ForeignKey(get_user_model(), verbose_name="スタッフ名", on_delete=models.CASCADE)
    


class SubmitAttendance(models.Model):
    class Meta:
        db_table = 'attendance'
    staff = staff = models.ForeignKey(get_user_model(), verbose_name="スタッフ", on_delete=models.CASCADE)
    place = models.ManyToManyField(Place, verbose_name='出勤場所')
    in_out = models.CharField(verbose_name='IN/OUT',max_length=3)
    time = models.DateTimeField(verbose_name="打刻時間", auto_now=False, auto_now_add=True)

