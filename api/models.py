from django.db import models

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    slug = models.SlugField(max_length=1000)
    image = models.ImageField()
    createdAt = models.DateTimeField(auto_now_add=True)
    lastEdited = models.DateTimeField(auto_now=True)
    authorName = models.CharField(max_length=100)
    def __str__(self):
        return f'Title: {self.title} Author: {self.authorName}'

class Comment(models.Model):
    content = models.TextField()
    userName = models.CharField(max_length=100)
    timePosted = models.DateTimeField(auto_now_add=True)
    blogId = models.ForeignKey('BlogModel', on_delete=models.CASCADE)
    def __str__(self):
        return f'Comment Author: {self.userName}'

class Category(models.Model):
    title:models.CharField(max_length = 200)
    def __str__(self):
        return self.title
class Image(models.Model):
    name: models.CharField(max_length=200)
    imageData: models.TextField()
    imageType: models.CharField(max_length=10)
    blogId: models.ForeignKey('BlogModel', on_delete=models.CASCADE)
    def __str__(self):
        return self.name




