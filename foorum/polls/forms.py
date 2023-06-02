
from django import forms
from .models import Question, Response

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