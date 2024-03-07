from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

def users_list(request):
    users = User.objects.all()
    return render(request, 'adminhomepage.html', {'users': users})
