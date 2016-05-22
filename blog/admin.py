from django.contrib import admin
from .models import Post, Comment, Question, Exam, ExamTemplate

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(Exam)
admin.site.register(ExamTemplate)
