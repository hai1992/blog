from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import markdown
from django.utils.html import strip_tags


class Category(models.Model):
    '''文章分类表'''
    name = models.CharField(max_length=30,verbose_name='分类名')
    class Meta:
        db_table='category'

class Tag(models.Model):
    """标签表"""

    name = models.CharField(max_length=80,verbose_name='标签名')
    class Meta:
        db_table='Tag'

class Post(models.Model):
    """文章表"""
    title = models.CharField(max_length=70,verbose_name='标题')
    body = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    excerpt = models.CharField(blank=True,verbose_name='摘要',max_length=300)
    category = models.ForeignKey(Category,related_name='post')
    tag = models.ManyToManyField(Tag, related_name='post')
    user = models.ForeignKey(User,related_name='post')
    views = models.PositiveIntegerField(default=0)
    class Meta:
        db_table='post'
        ordering=['-create_time']

    def save(self, *args,**kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt=strip_tags(md.convert(self.body))[:40]
        super().save(*args,**kwargs)





