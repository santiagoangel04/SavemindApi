from rest_framework.views import APIView
from .serializers import SavemindTranlateSerializer
from rest_framework.response import Response
from .models import SavemindTranlate


class TranslateWordView(APIView):
    def post(self,request):
        data = request.data
        dataTranslateToSave = SavemindTranlate(
            from_language = data.get('from_language'),
            to_language = data.get('to_language'),
            word = data.get('word'),
            context_word_use = data.get('context_word_use')
        )
        dataTranslateToSave.translate_word()
        serializerResponse = SavemindTranlateSerializer(dataTranslateToSave)
        return Response(serializerResponse.data)
    
    def get(self, request):
        data = request.data
        infoTranslateData = SavemindTranlate.objects.all()
        serializerDataTranslate = SavemindTranlateSerializer(infoTranslateData,many = True)
        return Response(serializerDataTranslate.data)