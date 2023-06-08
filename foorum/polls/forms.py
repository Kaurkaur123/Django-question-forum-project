
from django import forms
from .models import Question, Response#, Choice

#class CommentForm(forms.ModelForm):
#    class Meta:
#        model = Comment
#        fields = ('name', 'body')
class NewResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['body']

class NewReplyForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'What are your thoughts?'
            })
            }    
class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title',]
        widgets = {
            'title': forms.TextInput(attrs={
                'autofocus': True,
                'placeholder': 'Ask an interesting question (Please click BACK after submitting the question)'
            })
        }