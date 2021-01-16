from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import Note
from .serializers import NoteSerializer

# Details of a particular note. I have used slug to distinguish between notes.
@api_view(['GET',])
def details(request, slug):
    
    try:
        note = Note.objects.get(slug = slug)
        print(note)
    except Note.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
       serializer = NoteSerializer(note)
       return Response(serializer.data)

@api_view(['POST'])
def create(request):
    data = request.data
    note = Note.objects.create(title = data['title'], content = data['content'],slug = data['slug'])
    print(note)
    serializer = NoteSerializer(data =data, many=False)
    data = {}
    serializer.is_valid()
    serializer.save()
    data["success"] = "successful"
    print(serializer.data)
    return Response(serializer.data)
    
@api_view(['GET',])
def title_list(request):

    try:
        notes = Note.objects.all()
        list_of_title = []
        for note in notes:
            list_of_title.append(note.title)
        return JsonResponse(list_of_title, safe = False)

    except Note.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    

@api_view(['PUT'])
def update_note(request, slug):
    
    try:
        note = Note.objects.get(slug = slug)
    except Note.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = NoteSerializer(note, data = request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data = data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['DELETE'])
def delete_note(request, slug):
    
    try:
        note = Note.objects.get(slug = slug)
    except Note.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = note.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
            return Response(data = data)


