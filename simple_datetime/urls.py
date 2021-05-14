from django.urls import path
from . import views

urlpatterns = [
    path('now/', views.current_datetime),
    path('past/', views.past_datetime),
    path('404/', views.datetime_404),
]
