from django.shortcuts import render
from .models import Course


def index(request):
    courses = Course.objects.all()
    context = {
        courses: courses
    }
    return render(request, 'index.html', context)
