from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email"]


    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            check_email = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email is already in use')
            

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["username", 'body'] 

