from django.urls import path
from . import views # ←これ忘れないようにする！！

app_name = 'attendance'
urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
]