from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'thumbnail',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)