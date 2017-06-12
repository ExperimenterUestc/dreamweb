# coding=utf-8

from django import forms
from django.contrib import auth
from BlogManage.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ArticleForm,self).__init__(*args,**kwargs)
        self.fields['name'].label=u'名 称'
        self.fields['name'].error_messages={'required':u'请输入名称'}
        self.fields['text'].label=u'内 容'
        self.fields['text'].error_messages={'required':u'请输入内容'}



