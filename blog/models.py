from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import uuid


# Create your models here.


class Post(models.Model):
    post_id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to="image")
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
