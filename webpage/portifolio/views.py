from django.shortcuts import render
from .models import Profile


def about_me(request):
    TEMPLATE_NAME = "me.html"
    return render(request, TEMPLATE_NAME)


def index(request):
    TEMPLATE_NAME = "index.html"
    context = {
        "profile": Profile.objects.prefetch_related("links").first(),
        "projects": [{
            "name":"BackLess",
            "short_description": "Um removedor de backgrounds de imagens que utiliza tarefas assíncronas e arquitetura serverless. Projeto criado usando Django, Channels, Redis, Postgre, Google Cloud e AWS.",
            "active": True,
            "source": "https://github.com/marconi-dev"
        },{
            "name":"Flashcards API",
            "short_description": "Uma API REST para estudos com repetição espaçada inspirada no anki web. Criada com Django e Postgre, implementa autenticação JWT.",
            "status": "disable",
            "has_detail": True,
            "source": "https://github.com/marconi-dev"
        }]
    }
    
    return render(request, TEMPLATE_NAME, context)
