from django import forms
from .models import Question, Choice
from django.contrib.auth.forms import AuthenticationForm

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'tag')

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('id', 'question', 'choice_text', 'votes')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))