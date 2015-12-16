#-*- coding: utf-8 -*-

from django import forms


class genreArticle(forms.Form):
	genre=forms.CharField(max_length=100,)