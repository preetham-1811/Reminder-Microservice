from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer, TaskRegisterSerializer
from .models import Task
import jwt, datetime
from django.db.models import Q

@api_view(['GET'])
def List(request):
    try:
        token = request.COOKIES.get('jwt')
        payload = jwt.decode(token, 'secret-app-key', algorithms=['HS256'])
        user = payload['username']
        tasks = Task.objects.filter(Q(author=user) | Q(public=True)).order_by('-id')  # filter
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data,{'msg': 'Item deleted successfully'}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'msg': 'You do not have log in first to see items!'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
def Detail(request, pk):
    try:
        token = request.COOKIES.get('jwt')
        payload = jwt.decode(token, 'secret-app-key', algorithms=['HS256'])
        user = payload['username'] 
        tasks = Task.objects.get(id=pk, author=user)
        serializer = TaskSerializer(tasks, many=False)
        return Response(serializer.data)
    except Exception as err:
        return Response({'msg': 'You do not have log in first to see this item!'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def Create(request):
    serializer = TaskRegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def Update(request, pk):
    token = request.COOKIES.get('jwt')
    payload = jwt.decode(token, 'secret-app-key', algorithms=['HS256'])

    # user = User.objects.get(email=payload['email'])
    user = payload['username']

    try:
        task = Task.objects.get(id=pk,author=user)
        serializer = TaskSerializer(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    except Exception as err:
        return Response({'msg': 'You do not have access to this item!'}, status=status.HTTP_403_FORBIDDEN)



@api_view(['DELETE'])
def Delete(request, pk):
    token = request.COOKIES.get('jwt')
    payload = jwt.decode(token, 'secret-app-key', algorithms=['HS256'])

    user = payload['username']

    try:
        task = Task.objects.get(id=pk, author=user)
        task.delete()
        return Response({'msg': 'Item deleted successfully'}, status=status.HTTP_200_OK)

    except Exception as err:
        return Response({'msg': 'You do not have access to this item!'}, status=status.HTTP_403_FORBIDDEN)