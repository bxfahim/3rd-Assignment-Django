from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.title)
        super().save(*args, **kwargs)


class Post(models.Model):
    status = [
        ('draft','Draft'),
        ('publish','Published')
    ]

    title = models.CharField(max_length=200, help_text='Enter Your Post Title')
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    post_status = models.CharField(max_length=50, choices=status, default='draft')
    featured = models.BooleanField(default=False)
    featured_image = models.ImageField(upload_to ='uploads/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    meta_title = models.CharField(max_length=200, null=True, blank=True)
    meta_description = models.CharField(max_length=300, null=True, blank=True)


    def __str__(self):
        return self.title


    class Meta:
        ordering = ['created']


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.title)
        super().save(*args, **kwargs)




# Creating comment here.

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

