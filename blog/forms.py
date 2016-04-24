from django import forms

from .models import Post, Comment, Question


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('text', 'alternativeA', 'alternativeB', 'alternativeC', 'alternativeD', 'alternativeE')
