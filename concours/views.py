from django.shortcuts import render


def accueil(request):
    """Accueil de la partie Concours"""
    return render(request, concours/accueil.html)

def actualites(request):
    """Actualités du concours"""
    return render(request, concours/actualites.html)

def contact(request):
    """Formulaire de contact"""
    # ajouter le formulaire
    return render(request, concours/contact.html)

def equipe(request):
    """Page de présentation de l'équipe et du binet"""
    return render(request, concours/equipe.html)

def partenaires(request):
    """Page de présentation de nos partenaires"""
    return render(request, concours/partenaires.html)