from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            "user": request.user,
            "hw": "Hello World!"
        }
        return render(request, 'attendance/index.html', context)
index = IndexView.as_view()