# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('concours.views',
    # Une string vide indique la racine : on renvoie l'accueil
    url(r'^$', 'accueil', name='url_accueil'),
    # Page de presentation de l'equipe (le binet)
    url(r'^equipe$', 'equipe', name='url_equipe'),
    # Page de presentation des partenaires du concours
    url(r'^partenaires$', 'partenaires', name='url_partenaires'),
    # Page de contact
    url(r'^contact$', 'contact', name='url_contact'),
    # Page recensant les actualites (infos, presse...)
    url(r'^actualites$', 'actualites', name='url_actualites'),
    # Page permettant de lire en détail un article (actualité, partenaire ...)
    url(r'^lire/(?P<id>\d+)$', 'lire', name='lire_article'),
    # Page affichant la liste de tous les articles (actualités / partenaires ...)
    url(r'^articles$' , 'allArticles', name='allArticles')

)