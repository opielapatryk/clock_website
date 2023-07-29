from django.urls import path
from real_time_clock import views
urlpatterns = [
    path('', views.index, name='index'),
]