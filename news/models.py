from django.db import models

# Create your models here.

class Creator(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Article(models.Model):
    author = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name="articles")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    body = models.TextField()
    city = models.CharField(max_length=100)
    publish_date = models.DateField()
    is_active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title