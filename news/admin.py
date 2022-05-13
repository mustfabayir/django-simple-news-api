from django.contrib import admin
from news.models import Article, Creator
# Register your models here.

admin.site.register(Article)
admin.site.register(Creator)