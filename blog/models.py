from django.db import models
import os
from django.contrib.auth.models import User
from django.utils import timezone



class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'
    
    class Meta:
        verbose_name_plural = 'Categories'

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)

    category = models.ForeignKey(Category, null=True,blank=True,  on_delete=models.SET_NULL)

    tags = models.ManyToManyField(Tag, blank=True)

    like = models.ManyToManyField(User, related_name='likes', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    comment_count = models.PositiveIntegerField(default=0)

    views = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
    
    @property
    def update_counter(self):
        self.views = self.views + 1
        self.save()
        return self.views

    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    like = models.ManyToManyField(User, related_name='c_likes', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'
    



class ReComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.parent_comment.get_absolute_url()}#recomment-{self.pk}'
