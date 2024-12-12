from django.shortcuts import render

# Create your views here.



from django.shortcuts import render
from .models import Course

def home(request):
    courses = Course.objects.prefetch_related('students').all()
    return render(request, "projec1.html", {"courses": courses})

