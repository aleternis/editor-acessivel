# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Question, Exam, ExamTemplate, Option, Essay
from django.utils.translation import ugettext_lazy as _


class UserCreateForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _("Senhas diferentes."),
    }
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        
        self.fields['email'].required = True
        self.fields['email'].label = u"Email"
        self.fields['username'].help_text = "Somente letras, dígitos e @/./+/-/_"
        self.fields['username'].label = u"Usuário"
        self.fields['password1'].label = u"Senha"
        self.fields['password2'].label = u"Confirme sua senha"
        self.fields['password1'].help_text = "A senha deve conter pelo menos 8 caracteres e conter letras e digítos."
        self.fields['password2'].help_text = "Repita a senha para verificação."


    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class ExamForm(forms.ModelForm):

    class Meta:
        model = Exam
        fields = ('title', 'template')

class ExamTemplateForm(forms.ModelForm):

    class Meta:
        model = ExamTemplate
        fields = ('name', 'questions', 'answers', 'essay')

class QuestionForm(forms.ModelForm):

	class Meta:
		model = Question
		fields = ('text',)

class EssayForm(forms.ModelForm):

    class Meta:
        model = Essay
        fields = ('text',)

class OptionForm(forms.ModelForm):

    class Meta:
        model = Option
        fields = ('option',)