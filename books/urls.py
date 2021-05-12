from django.urls import path
from books.views import PublisherListView, PublisherDetailView

app_name = 'books'
urlpatterns = [
    path('publishers/', PublisherListView.as_view(), name='publishers'),
    path('publishers/<int:pk>/', PublisherDetailView.as_view(), name='publisher_detail'),
]
