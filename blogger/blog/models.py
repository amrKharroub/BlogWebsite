from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, null=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField()
    tags = TaggableManager()

    class Meta:
        ordering = ("-created_at",)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return self.title
