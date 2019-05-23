from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
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

    
class CulculateFee(models.Model):
    '''
    class Meta:
        db_table = 'fee'
    #date = SubmitAttendance.objects.filter('date')
    start = SubmitAttendance.objects.get(in_out=1, staff_id=9).time
    end = SubmitAttendance.objects.get(in_out=0, staff_id=9).time
    howlong_hours = ((end - start).seconds) / 3600
    fee = howlong_hours * 900 
    def culculatedFee(self):
        self.save()
    '''



