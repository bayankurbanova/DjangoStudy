

TestMiddleware:

def__init__(self, get_response):
    self._get_response = get_response


def__call__(self, request):
    return self._get_response(request)

def process_view(self, request, views_func, views_args, views_kwargs):
    print()
