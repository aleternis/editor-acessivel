# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


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

class ExamTemplate(models.Model):
    name = models.CharField(max_length=300, verbose_name=_(u'Insira o título do novo template de prova'))
    questions = models.IntegerField(verbose_name=_(u'Insira a quantidade de questões'))
    answers = models.IntegerField(verbose_name=_('Insira a quantidade de alternativas'))
    essay = models.BooleanField(verbose_name=_(u'Marcar caso deseja incluir redação a esse template'))

    class Meta:
        permissions = (
            ("exam_template_list", "Can see template list"),
            ("exam_template_detail", "Can see template detail"),
        )

    def __str__(self):
        return self.name

class Exam(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=300, verbose_name=_(u'Insira o título da sua prova'))
    template = models.ForeignKey('blog.ExamTemplate', verbose_name=_(u'Escolha o modelo de template que será usado na sua prova'))

    class Meta:
        permissions = (
            ("exam_list", "Can see exam list"),
            ("exam_detail", "Can see exam detail"),
        )

    def __str__(self):
        return self.title

class Option(models.Model):
    question = models.ForeignKey('blog.Question')
    option = HTMLField(verbose_name=_(u'Insira o texto da alternativa sem a letra'))

class Essay(models.Model):
    exam = models.ForeignKey('blog.Exam')
    text = HTMLField(u'Insira o enunciado da redação')

class Question(models.Model):
    exam = models.ForeignKey('blog.Exam')
    text = HTMLField(u'Insira o enunciado da questão sem a sua numeração')
    sequence = models.IntegerField()

    class Meta:
        permissions = (
            ("question_list", "Can see question list"),
            ("question_detail", "Can see question detail"),
        )

    def create(self):
        self.save()

    def __str__(self):
        return str(self.sequence)

  





