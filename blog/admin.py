from django.contrib import admin
from .models import Question, Exam, ExamTemplate, Essay

admin.site.register(Question)
admin.site.register(Exam)
admin.site.register(ExamTemplate)
admin.site.register(Essay)
