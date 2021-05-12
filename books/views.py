from django.views.generic import ListView, DetailView
from books.models import Publisher, Book


class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'


class PublisherDetailView(DetailView):
    model = Publisher
    # context_object_name = 'publisher'
    # template_name = 'books/publisher_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context
