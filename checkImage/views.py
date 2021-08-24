from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from snippets.models import Snippet
#from snippets.serializers import SnippetSerializer
from checkImage.models import checkImage
from checkImage.serializers import CheckSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def check_list(request, format=None):
    if request.method == 'GET':
        images = checkImage.objects.all()
        serializer = CheckSerializer(images, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CheckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

