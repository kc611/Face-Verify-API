from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PersonSerializer,FaceSerializer,FaceEmbeddingSerializer
from .models import Person,Face
from .verification_model import verify_image_class


@api_view(['GET'])
def api_overview(request):
    # Also Include Details or redirect to a page
    api_urls = {
        'List of all Users registered':'/list/',
        'Details of a User': '/details/<str:id>',
        'Create a User':'/create/',
        'Update a User':'/update/<str:id>',
        'Verify a Photo':'/verify/',
        'Delete a User':'/delete/<str:id>',
    }
    return Response(api_urls)

class person():
    @api_view(['GET'])
    def list_all(request):
        curr_person = Person.objects.all()
        serializer = PersonSerializer(curr_person,many = True)
        return Response(serializer.data)

    @api_view(['POST'])
    def create_person(request):
        serializer = PersonSerializer(data= request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @api_view(['POST'])
    def update_person(request,id):
        curr_person = Person.objects.get(id = id)

        serializer = PersonSerializer(instance = curr_person,data= request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @api_view(['DELETE'])
    def delete_person(request,id):
        curr_person = Person.objects.get(id = id)
        curr_person.delete()
        return Response("Object Deleted Sucessfully")

class face():
    @api_view(['GET'])
    def list_all(request):
        curr_face = Face.objects.all()
        serializer = FaceSerializer(curr_face,many = True)
        return Response(serializer.data)
    
    @api_view(['GET'])
    def list_by_person(request,id):
        curr_face = Face.objects.all()
        serializer = FaceSerializer(curr_face,many = True)
        return Response(serializer.data)

    @api_view(['POST'])
    def add_image(request):
        request.data._mutable = True
        request.data['embeddings'] = verify_image_class.create_embeddings(request.data['image_data'])
        
        request.data._mutable = False

        serializer = FaceSerializer(data = request.data)
        serializer.is_valid(raise_exception=True )
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @api_view(['POST'])
    def update_image(request,id):
        curr_image = Face.objects.get(id = id)
        serializer = FaceSerializer(instance = curr_image,data= request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    @api_view(['DELETE'])
    def delete_image(request,id):
        curr_face = Face.objects.get(id = id)
        curr_face.delete()
        return Response("Object Deleted Sucessfully")

class verify_image():
    @api_view(['POST'])
    def linear_verify(request):
        
        curr_embeds = verify_image_class.create_embeddings(request.data['image_data'])
        
        min_dist,face_id = verify_image_class.return_distance(curr_embeds)

        curr_person = Person.objects.get(id = face_id)

        serializer = PersonSerializer(curr_person)

        return Response("Min Dist is "+str(min_dist)+" from "+str(serializer.data['name']))

class dev():
    @api_view(['GET'])
    def return_embeddings(request,id):
        curr_face = Face.objects.get(id = id)
        serializer = FaceEmbeddingSerializer(curr_face)
        return Response(serializer.data)
    