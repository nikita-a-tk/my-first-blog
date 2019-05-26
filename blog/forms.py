from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'thumbnail',)
        widgets = {
            'title': forms.TextInput(attrs = {'placeholder': "Title",
                                             'class': "form-control"}),
            'text': forms.Textarea(attrs = {'placeholder': "Type your text",
                                            'class': "form-control",
                                            'rows': 7}),
            # 'thumbnail': forms.FileInput(attrs = {})
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
        widgets = {
            'author': forms.TextInput(attrs = {'id': "username",
                                             'placeholder': "Name",
                                             'class': "form-control"}),
            'text': forms.Textarea(attrs = {'id': "usercomment",
                                            'placeholder': "Type your comment",
                                            'class': "form-control",
                                            'rows': 4}),
        }

        