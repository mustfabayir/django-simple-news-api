from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from news.models import Article, Creator
from news.api.serializers import ArticleSerializer, CreatorSerializer

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class CreatorListApiView(APIView):
    def get(self, request):
        authors = Creator.objects.all()
        serializer = CreatorSerializer(authors, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = CreatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleListApiView(APIView):
    def get(self, request):
        articles = Article.objects.filter(is_active=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailView(APIView):

    def get_object(self, pk):
        article_instance = get_object_or_404(Article, pk=pk)
        return article_instance

    def get(self, request, pk):
        article_instance = self.get_object(pk=pk)
        serializer = ArticleSerializer(article_instance)
        return Response(serializer.data)

    def put(self, request, pk):
        article_instance = self.get_object(pk=pk)
        serializer = ArticleSerializer(article_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article_instance = self.get_object(pk=pk)
        article_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




