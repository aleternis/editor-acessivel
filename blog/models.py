from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
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
    text = HTMLField()
    alternativeA = HTMLField()
    alternativeB = HTMLField()
    alternativeC = HTMLField()
    alternativeD = HTMLField()
    alternativeE = HTMLField()

    def clean(self):
        output = self.verify_paragraph_length(self.text)
        if output:
            raise ValidationError(output)

    def create(self):
        self.save()

    def __str__(self):
        return self.id

    def verify_paragraph_length(self, text):
        sentences = text.split("</p>")
        alt = 'alt=""'
        output = []
        for index, i in enumerate(sentences, start=1):
            if len(i.split()) > 10:
                output.append('paragraph %d is too long' % index)
            if alt in i:
                output.append('imagem sem descricao')
        return output





