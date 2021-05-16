from django.urls import include, path
from myapp.views import MyClassView, GreetingView, MorningGreetingView

urlpatterns = [
    path('about/', MyClassView.as_view()),
    path('greeting/', include([
        path('', GreetingView.as_view()),
        # path('', GreetingView.as_view(greeting="G'Day")),
        path('morning/', MorningGreetingView.as_view()),
    ]))
]
