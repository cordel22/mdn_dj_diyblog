from django.forms import ModelForm
from .models import Post, Comment
#   from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


'''
class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
'''

"""
class CreatePostForm(forms.Form):
    #   renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    
    name = forms.CharField(max_length=200)

    author = forms.CharField('Author', on_delete=models.SET_NULL, null=True)

    
    content = forms.TextField(max_length=1000, help_text='Enter the blog Post content')
    
    topic = forms.ChoiceField(Topic, help_text='Select a Topic for this blog Post')
    
    '''
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data
    '''
"""   
    