from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from main.models import News


@login_required
def publish_news(request, news_id):
    try:
        news = News.objects.get(id=news_id)
        news.published = True
        news.save()

        msg = 'success'
        status_code = 200
        messages.success(request, 'The news has been successfully published!')
    except News.DoesNotExist:
        msg = 'error'
        status_code = 400
        messages.error(request, "The news doesn't exists!")

    return JsonResponse({'msg': msg}, status=status_code)


def find_news(request):
    news_list = request.GET.getlist('newsList[]')
    exist_new_news = News.objects.filter(published=True).exclude(id__in=news_list).exists()
    return JsonResponse({'message': exist_new_news}, status=200)
