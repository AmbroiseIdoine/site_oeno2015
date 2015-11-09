# -*- coding: utf-8 -*-

from django.db import models

class Article(models.Model):

	Actualites = 'AC'
	Partenaires = 'PA'

	GENRE = ( (Actualites, 'Actualités'), (Partenaires, 'partenaires'), )

	genre = models.CharField(max_length=2, choices=GENRE, default=Actualites)
	titre = models.CharField(max_length=200)
	image = models.ImageField(upload_to='img', null=True, blank=True)
	contenu = models.TextField(null=True)
	date = models.DateTimeField(auto_now_add=True, auto_now=False, 
								verbose_name="Date de parution")
	
	def __str__(self):
		""" 
		Cela stocke des articles avec un titre, une photo et un texte asocié
		"""
		return self.titre



