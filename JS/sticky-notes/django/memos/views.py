from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Memo
from .serializers import MemoSerializer


@api_view(['GET', 'POST'])
def memos_list(request):
    if request.method == "GET":
        memos = Memo.objects.all()
        serializer = MemoSerializer(memos, many=True)
        return Response(serializer.data)
    else:
        serializer = MemoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def delete_memo(request, pk):
    memo = get_object_or_404(Memo, id=pk)
    memo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
