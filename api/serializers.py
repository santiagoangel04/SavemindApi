#serializer words
from rest_framework import serializers
from api.models import SavemindTranlate

class SavemindTranlateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    word = serializers.CharField(required = True)
    
    class Meta:
        model = SavemindTranlate
        fields = ['id','from_language','to_language','word','translated_Word','context_word_use','status']