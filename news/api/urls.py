from django.urls import path
from news.api import views as api_views

urlpatterns = [
    path('creators/', api_views.CreatorListApiView.as_view(), name='creator_list'),
    path('articles/', api_views.ArticleListApiView.as_view(), name='article_list'),
    path('articles/<int:pk>', api_views.ArticleDetailView.as_view(), name='article-detail'),
]