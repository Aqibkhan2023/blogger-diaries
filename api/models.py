from django.db import models
from django.db.models.fields import TextField
from django.utils.text import slugify
from froala_editor.fields import FroalaField



class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=250)
    content = TextField()#FroalaField()
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
    
    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            # will remove spaces in the product name and replace it with hyphen/ underscore
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)


class Comment(models.Model):
    content = FroalaField()
    userName = models.CharField(max_length=100)
    timePosted = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-timePosted",)

    def __str__(self):
        return f'Comment Author: {self.userName}'


class Image(models.Model):
    name = models.CharField(max_length=200)
    imageData = models.TextField()
    imageType = models.CharField(max_length=10)
    blog = models.ForeignKey(Blog, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# get all ----------------------------------------done [(Pagination) query limit, offset]   
# get particlu :id -------------------------------done
# get comments on a blog (blog id)
# create comment (blog id)