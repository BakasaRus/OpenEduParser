from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>', views.show, name='show'),
    path('update', views.update, name='update'),
]
