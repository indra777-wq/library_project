from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .models import Book, Comics
from .serializers import BookGetSerializer, GetSerializer
from rest_framework import generics


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookGetSerializer


# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookGetSerializer

#
# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookGetSerializer


# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookGetSerializer

# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookGetSerializer


class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookGetSerializer


class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookGetSerializer


class BookListApiView(APIView):
    def get(self, requests):
        books = Book.objects.all()
        serializer_data = GetSerializer(books, many=True).data

        data = {
            'status': f'returned - {len(books)}',
            'books': serializer_data
        }
        return Response(data)


class BookCreateApiView(APIView):
    def post(self, request):
        serializer = BookGetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return (Response({
                'status': 'Book created successfully',
                'book': serializer.data
            }, status=status.HTTP_201_CREATED))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailApiView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        serializer_data = BookGetSerializer(book).data

        return Response(serializer_data)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookGetSerializer


class BookDeleteApiView(APIView):
    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response({
            'status': 'Book deleted successfully',
        })

    # except Book.DoesNotExist:
    #     return Response({
    #         'error': 'Book not found'
    #     }, status=status.HTTP_404_NOT_FOUND)
    #


class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookGetSerializer(book, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                'status': 'Book updated successfully',
                'book': serializer.data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComicsUpdateApiView(APIView):
    def put(self, request, pk):
        comics = get_object_or_404(Comics, pk=pk)
        serializer = GetSerializer(instance=comics, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                'status': 'Book updated successfully',
                'book': serializer.data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComicsListApiView(APIView):
    def get(self, requests):
        comics = Comics.objects.all()
        serializer_data = GetSerializer(comics, many=True).data

        data = {
            'status': f'returned - {len(comics)}',
            'books': serializer_data
        }
        return Response(data)
