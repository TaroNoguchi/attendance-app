from django.urls import path
from . import views # ←これ忘れないようにする！！

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]