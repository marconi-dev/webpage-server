from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer


class IndexAPIView(APIView):
    http_method_names = ("get",)

    def get_profile_data(self):
        profile = Profile.objects.prefetch_related('links').first()
        profile_serializer = ProfileSerializer(profile)
        return profile_serializer.data

    # context = {
    #     "profile": Profile.objects.prefetch_related("links").first(),
    #     "projects": [{
    #         "name":"BackLess",
    #         "short_description": "Um removedor de backgrounds de imagens que utiliza tarefas assíncronas e arquitetura serverless. Projeto criado usando Django, Channels, Redis, Postgre, Google Cloud e AWS.",
    #         "active": True,
    #         "source": "https://github.com/marconi-dev"
    #     },{
    #         "name":"Flashcards API",
    #         "short_description": "Uma API REST para estudos com repetição espaçada inspirada no anki web. Criada com Django e Postgre, implementa autenticação JWT.",
    #         "status": "disable",
    #         "has_detail": True,
    #         "source": "https://github.com/marconi-dev"
    #     }]
    # }
    
    def get(self, request, *args, **kwargs):
        profile_data = self.get_profile_data()
        response_data = {
            'profile': profile_data
        }
        return Response(response_data, status=status.HTTP_200_OK)
