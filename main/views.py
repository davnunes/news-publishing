from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from main.forms import NewsForm, AuthorForm
from main.models import News, Author


def index(request):
    news_queryset = News.objects.filter(published=True)
    list_news_id = [news.id for news in news_queryset]
    context = {
        'newsList': news_queryset,
        'listNewsId': list_news_id
    }
    return render(request, 'main/home.html', context)


@login_required
def home_admin(request):
    news = News.objects.all()
    context = {
        'newsList': news,
    }
    return render(request, 'main/home_admin.html', context)


@login_required
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'News created successfully!')
            return redirect('home_admin')
        else:
            messages.error(request, 'Please fill out the fields correctly!')
    else:
        form = NewsForm()

    context = {
        'form': form
    }
    return render(request, 'news/create_update.html', context)


@login_required
def news_update(request, news_id):
    news = get_object_or_404(News, id=news_id)

    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            news.modified_in = datetime.now()
            form.save()

            messages.success(request, 'News changed successfully!')
            return redirect('news_update', news_id)
        else:
            messages.error(request, 'Please fill out the fields correctly!')
    else:
        form = NewsForm(instance=news)

    context = {
        'form': form,
        'news': news
    }
    return render(request, 'news/create_update.html', context)


@login_required
def news_delete(request, news_id):
    news = get_object_or_404(News, id=news_id)
    news.delete()

    messages.success(request, 'News deleted successfully!')
    return JsonResponse({'msg': 'success'})


def author_list(request):
    authors = Author.objects.all()
    context = {
        'authorsList': authors
    }
    return render(request, 'author/list.html', context)


def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Author created successfully!')
            return redirect('author_list')
        else:
            messages.error(request, 'Please fill out the fields correctly!')
    else:
        form = AuthorForm()

    context = {
        'form': form
    }
    return render(request, 'author/create_update.html', context)


@login_required
def author_update(request, author_id):
    author = get_object_or_404(Author, id=author_id)

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()

            messages.success(request, 'Author changed successfully!')
            return redirect('author_list')
        else:
            messages.error(request, 'Please fill out the fields correctly!')
    else:
        form = AuthorForm(instance=author)

    context = {
        'form': form,
        'author': author
    }
    return render(request, 'author/create_update.html', context)


@login_required
def author_delete(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    author.delete()

    messages.success(request, 'Author deleted successfully!')
    return JsonResponse({'msg': 'success'})
