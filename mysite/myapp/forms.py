#coding:utf-8
from django import forms

class IntForm(forms.Form):
    year=forms.IntegerField(label = '年份')
    episode = forms.IntegerField(label = '集数')


class ChaForm(forms.Form):
    year=forms.IntegerField(required=False)
    episode = forms.IntegerField(required=False)
class UserForm(forms.Form):    
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
 

