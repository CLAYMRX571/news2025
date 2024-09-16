from django.db import models
from home.models import User 
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract=True 

class Category(BaseModel):
    name = models.CharField(max_length=255) 
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

class Tag(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Article(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(upload_to='articles')
    description = RichTextUploadingField()
    views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles') 
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True)
    
    def __str__(self):
        return f"{self.id} {self.title}"

class Contact(BaseModel):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
