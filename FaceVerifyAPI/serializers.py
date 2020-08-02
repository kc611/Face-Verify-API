from rest_framework import serializers
from .models import Person,Face

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class FaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Face
        fields = '__all__'

class FaceEmbeddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Face
        fields = ['embeddings']
            