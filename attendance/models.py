from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import datetime as dt
from django.utils import timezone

# Create your models here.
class SubmitAttendance(models.Model):
    
    class Meta:
        db_table = 'attendance'
    
    PLACES = (
        (1, 'TANKS'),
        (2, 'Red Tails'),
        (3, 'ANNIE HALL'),
        (4, 'NOKUROXY'),
        (5, '七'),
        (6, 'ART MON ZEN'),
    )
    IN_OUT = (
        (1, 'IN'),
        (0, 'OUT'),
    )

    staff = models.ForeignKey(get_user_model(), verbose_name="スタッフ", on_delete=models.CASCADE, default=None)
    place = models.IntegerField(verbose_name='出勤場所名', choices=PLACES, default=None)
    in_out = models.IntegerField(verbose_name='IN/OUT', choices=IN_OUT, default=None)
    time = models.TimeField(verbose_name="打刻時間")
    date = models.DateField(verbose_name='打刻日')

    #辞書化
    place_dict = dict(PLACES)
    in_out_dict = dict(IN_OUT)

    def __str__(self):
        return  User.objects.get(id=self.staff_id), str(self.place_dict[self.place]), str(self.in_out_dict[self.in_out])
    
class Fee(SubmitAttendance):
    
    class Meta:
        db_table = 'fee'
    '''
    today = models.DateField(verbose_name='出勤日')
    staff = SubmitAttendance.staff()
    start = SubmitAttendance.objects.get(in_out=1, staff_id=staff, date=today).time
    end = SubmitAttendance.objects.get(in_out=0, staff_id=staff, date=today).time
    howlong_hours = ((end - start).seconds) / 3600
    fee = howlong_hours * 900
    '''


