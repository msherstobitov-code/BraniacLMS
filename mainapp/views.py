from django.http import HttpResponse
from django.views.generic import View


class HelloWorldView():
    def get(self, *args, **qwargs):
        return HttpResponse("Hello world")


def check_kwargs(request, **qwargs):
    return HttpResponse(f"kwargs:<br> {qwargs}")

