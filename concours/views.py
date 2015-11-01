#-*- coding: utf-8 -*-

from django.http import Http404
from django.shortcuts import render
from concours.models import Article

def accueil(request):
    """Accueil de la partie concours"""
    return render(request, 'concours/accueil.html')

def actualites(request):
    """Actualités du concours"""
    articles = Article.objects.filter(genre='AC') # Nous sélectionnons tous nos articles
    return render(request, 'concours/actualites.html', {'derniers_articles': articles})

def contact(request):
    """Formulaire de contact"""
    # ajouter le formulaire
    return render(request, 'concours/contact.html')

def equipe(request):
    """Page de présentation de l'équipe et du binet"""
    return render(request, 'concours/equipe.html')

def partenaires(request):
    """Page de présentation de nos partenaires"""
    return render(request, 'concours/partenaires.html')

def lire(request, id):
    try:
        article=Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'concours/lire.html', {'article': article})

def allArticles(request, id, genre):
    try:
        article=Article.objects.filter(genre=genre).orderBy(date)

    except Article.DoesNotExist:
        raise Http404
    return render(request, 'concours/allArticles.html', {'article': article, 'genre' : genre})
