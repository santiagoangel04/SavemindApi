from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView 
from .serializers import SavemindTranlateSerializer
from .models import SavemindTranlate
from rest_framework import status


#crud
class TranslateWordViewCR(APIView):
    def get(self, request):
        words_Translate = SavemindTranlate.objects.all()
        serializer_Get_Words = SavemindTranlateSerializer(words_Translate, many =True)
        return Response(serializer_Get_Words.data)
    
    def post(self,request):
        data = request.data

        #lleno cada uno de los atributos de mi clase que son los mismos datos de mi db
        dataTranslateToSave = SavemindTranlate(
            from_language = data.get('from_language'),
            to_language = data.get('to_language'),
            word = data.get('word'),
            context_word_use = data.get('context_word_use')
        )
        dataTranslateToSave.translate_word()
        serializerTranslateToSave = SavemindTranlateSerializer(dataTranslateToSave)
        return Response(serializerTranslateToSave.data)
  
class TranslateWordViewUD(APIView):

    def get_object_by_id(self,id):
        try:
            return SavemindTranlate.objects.get(pk = id)
        except: 
            raise Http404
        
    #obtener una palabra por id
    def get(self,request,id):
        object_by_id = self.get_object_by_id(id)
        serializer = SavemindTranlateSerializer(object_by_id)
        return Response(serializer.data)
        
    
    def patch(self,request,id):
        object_by_id = self.get_object_by_id(id)
        serializer = SavemindTranlateSerializer(object_by_id,data = request.data,partial =True )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self,request,id):
        pass
