from django import forms

from .models import Post, Comment, Question, Exam, ExamTemplate, Option


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class ExamForm(forms.ModelForm):

    class Meta:
        model = Exam
        fields = ('title', 'template')

class ExamTemplateForm(forms.ModelForm):

    class Meta:
        model = ExamTemplate
        fields = ('name', 'questions', 'answers')

class QuestionForm(forms.ModelForm):

	class Meta:
		model = Question
		fields = ('text',)

class OptionForm(forms.ModelForm):

    class Meta:
        model = Option
        fields = ('option',)