from django.http import HttpResponse
from django.views import View


def my_function_view(request):
    if request.method == 'GET':
        return HttpResponse('function view result')


class MyClassView(View):
    def get(self, request):
        return HttpResponse('class view result')


class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)


class MorningGreetingView(GreetingView):
    greeting = "Morning to ya"
