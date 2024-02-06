from django.http import HttpResponse, HttpResponseNotFound


def get_post(request, name_post: str):
    if name_post == 'dog':
        return HttpResponse('информация о блоге dog')
    elif name_post == 'charmander':
        return HttpResponse('информация о блоге charmander')
    else:
        return HttpResponseNotFound('страница не найдена')
