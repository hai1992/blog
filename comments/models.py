from django.db import models

# Create your models here.
from blogp.models import Post


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,related_name='comment')

    def __str__(self):
        return self.text[:20]

    class Meta:
        db_table = 'comment'
