from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TweetForm(forms.ModelForm):
    class Meta:
        model= Tweet
        fields = ['heading','text','photo',]

# class TweetForm(forms.ModelForm):
#     class Meta:
#         model = Tweet
#         fields = ['text', 'photo']
#         widgets = {
#             'text': forms.Textarea(attrs={'class': 'form-control'}),
#             'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#         }

class userRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    profile = forms.ImageField()
    dob = forms.DateField(input_formats=['%Y-%m-%d'], required=True)
    class Meta:
        model = User
        fields = ('username','email','password1','password2',)


    def __init__(self, *args, **kwargs):
        super(userRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['profile'].widget.attrs['class'] = 'form-control'
        self.fields['dob'].widget.attrs['class'] = 'form-control'
