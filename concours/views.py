#-*- coding: utf-8 -*-

from django.http import Http404
from django.shortcuts import render
from concours.models import Article
from concours.forms import genreArticle

def accueil(request):
    """Accueil de la partie concours"""
    return render(request, 'concours/accueil.html')

def actualites(request):
    """Actualités du concours"""
    form = genreArticle(request.POST)

    articles = Article.objects.filter(genre='AC').order_by("date")[:2] # Nous sélectionnons les 2 premiers articles
    return render(request, 'concours/actualites.html', {'derniers_articles': articles, "form":form})

def contact(request):
    """Formulaire de contact"""
    # ajouter le formulaire
    return render(request, 'concours/contact.html')

def equipe(request):
    """Page de présentation de l'équipe et du binet"""
    return render(request, 'concours/equipe.html')

def partenaires(request):
    """Page de présentation de nos partenaires"""
    articles = Article.objects.filter(genre='PA').order_by("date")[:2] # Nous sélectionnons les 2 premiers articles
    return render(request, 'concours/partenaires.html', {'derniers_articles': articles})

def lire(request, id):
    try:
        article=Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'concours/lire.html', {'article': article})

def allArticles(request):
    genre=''

    if request.method == 'POST':
        form = genreArticle(request.POST)  # Nous reprenons les données
        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            genre = form.cleaned_data['genre']

    try:
            article=Article.objects.filter(genre=genre).order_by("date")

    except Article.DoesNotExist:
        raise Http404
    return render(request, 'concours/allArticles.html', {'derniers_articles': article, 'genre' : genre})
