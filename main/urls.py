from django.urls import path

from main import views, api
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='home'),
    path('api/find_news/', api.find_news, name='find_news'),

    path('home-admin/', views.home_admin, name='home_admin'),
    path('news/create/', views.news_create, name='news_create'),
    path('news/update/<int:news_id>', views.news_update, name='news_update'),
    path('news/delete/<int:news_id>', views.news_delete, name='news_delete'),
    path('api/news/publish/<int:news_id>', api.publish_news, name='publish_news'),

    path('author/list/', views.author_list, name='author_list'),
    path('author/create/', views.author_create, name='author_create'),
    path('author/update/<int:author_id>', views.author_update, name='author_update'),
    path('author/delete/<int:author_id>', views.author_delete, name='author_delete'),

]
