from django.http.response import JsonResponse


def page(request, num=1):
    return JsonResponse({'blog_page': 'succeed ' + str(num)})


def history(request, page_slug, page_id):
    return JsonResponse(('history,', {'page_slug': page_slug, 'page_id': page_id}))


def edit(request):
    return JsonResponse({'edit': 'succeed'})


def discuss(request):
    return JsonResponse({'discuss': 'succeed'})


def permissions(request):
    return JsonResponse({'permissions': 'not allowed'})
