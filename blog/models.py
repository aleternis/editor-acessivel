from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Question(models.Model):
    text = RichTextField()
    alternativeA = RichTextField()
    alternativeB = RichTextField()
    alternativeC = RichTextField()
    alternativeD = RichTextField()
    alternativeE = RichTextField()
    
    def clean(self):
        if len(self.text) > 100:
            raise ValidationError(_('text is bigger than 100'))

    def create(self):
        self.save()

    def __str__(self):
        return self.text

