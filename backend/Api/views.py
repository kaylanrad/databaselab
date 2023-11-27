from rest_framework.views import APIView
from Api.models import Book
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework import status
import random
import string
from rest_framework.permissions import IsAuthenticated
from itertools import chain
from django.db.models import Q


class ShowAllBooksView(APIView):
    def get(self, request):
        books = Book.objects.all()
        data = []
        for book in books:
            data.append(
                {
                    'title': book.title,
                    'author': [a.full_name for a in book.author.all()],
                    'publisher': [p.full_name for p in book.publisher.all()],
                    'translator': [t.full_name for t in book.translator.all()],
                    'genre': [g.name for g in book.genre.all()],
                    'description': book.description
                }
            )
            
        return Response(data,status=status.HTTP_200_OK)


