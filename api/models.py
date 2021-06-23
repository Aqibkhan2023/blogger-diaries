from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.SlugField(max_length=1000)
    createdAt = models.DateTimeField(auto_now_add=True)
    lastEdited = models.DateTimeField(auto_now=True)
    publishedAt = models.DateTimeField(blank=True, null=True)
    authorName = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-publishedAt",)

    def __str__(self):
        return f'Title: {self.title} Author: {self.authorName}'


class Comment(models.Model):
    content = models.TextField()
    userName = models.CharField(max_length=100)
    timePosted = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment Author: {self.userName}'


class Image(models.Model):
    name = models.CharField(max_length=200)
    imageData = models.TextField()
    imageType = models.CharField(max_length=10)
    blog = models.ForeignKey(Blog, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
