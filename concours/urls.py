from django.conf.urls import patterns, url

urlpatterns = patterns('mini_url.views',
    # Une string vide indique la racine : on renvoie l'accueil
    url(r'^$', 'accueil', name='url_accueil'),
    # Page de présentation de l'équipe (le binet)
    url(r'^equipe$', 'equipe', name='url_equipe'),
    # Page de présentation des partenaires du concours
    url(r'^partenaires$', 'partenaires', name='url_partenaires'),
    # Page de contact
    url(r'^contact$', 'contact', name='url_contact'),
    # Page recensant les actualités (infos, presse...)
    url(r'^actualites$', 'actualites', name='url_actualites'),
)
