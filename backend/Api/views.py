from rest_framework.views import APIView
from Api.models import User, Book , Genre, Author, GateWay
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework import status
from Api.serializers import SignUpSerializer
import random
import string
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from itertools import chain
from django.db.models import Q
from django.shortcuts import get_object_or_404 



def rand_ascii(size):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))



class UserSecThrottle(UserRateThrottle):
    scope = 'signup'


class SignUp(APIView):
    throttle_classes = [UserSecThrottle]

    def post(self, request):
        try:
            ser = SignUpSerializer(data=request.data)
            if not ser.is_valid():
                return Response({"message": "مقادیر قابل قبول نیست"}, status=status.HTTP_400_BAD_REQUEST)
            phone_number = request.data.get('phone_number')
            username = request.data.get('username')
            password = request.data.get('password')
            email = request.data.get('email')

            if User.objects.filter(phone_number=phone_number).exists():
                return Response({"message": "این شماره تلفن قبلا ثبت شده"}, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(username=username).exists():
                return Response({"message": "این نام کاربری قبلا ثبت شده"}, status=status.HTTP_400_BAD_REQUEST)
            token = rand_ascii(100)
            user = User.objects.create_user(username=username, token=token, phone_number=phone_number, email=email, password=password)

            refresh = RefreshToken.for_user(user)


            return Response({"access": str(refresh.access_token), "refresh": str(refresh)}, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)



class ShowAllBooksView(APIView):
    def get(self, request):
        books = Book.objects.all()
        data = []
        for book in books:
            data.append(
                {
                    'id': book.id,
                    'title': book.title,
                    'author': [a.full_name for a in book.author.all()],
                    'publisher': [p.full_name for p in book.publisher.all()],
                    'translator': [t.full_name for t in book.translator.all()],
                    'genre': [g.name for g in book.genre.all()],
                    'description': book.description
                }
            )
        return Response(data,status=status.HTTP_200_OK)



class ShowSingleBook(APIView):
    def get(self, request):
        id = request.query_params.get('id')
        book = Book.objects.filter(id=id)
        data = []
        for b in book:
            data.append(
                {
                    'title': b.title,
                    'author': [a.full_name for a in b.author.all()],
                    'publisher': [p.full_name for p in b.publisher.all()],
                    'translator': [t.full_name for t in b.translator.all()],
                    'genre': [g.name for g in b.genre.all()],
                    'page_count': b.page_count,
                    'is_exist': b.is_exist,
                    'edition_year': b.edition_year,
                    'description': b.description,
                    'content': b.content

                }
            )
        return Response(data,status=status.HTTP_200_OK)



class ShowAllGenre(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        data = []
        for genre in genres:
            data.append(
                {
                    'name': genre.name,
                    'description' : genre.description
                }
            )
        return Response(data,status=status.HTTP_200_OK)
    


class ShowSingleGenre(APIView):
    def get(self, request):
        id = request.query_params.get('id')
        genre = Genre.objects.filter(id=id)
        data = []
        for g in genre:
            data.append(
                {
                    'name': g.name,
                    'description' : g.description
                }
            )
        return Response(data,status=status.HTTP_200_OK)



class ShowAllAuthor(APIView):
    def get(self, request):
        authors = Author.objects.all()
        data = []
        for author in authors:
            data.append({
                'full_name': author.full_name,
                'pen_name': author.pen_name,
                'description': author.description,
            })
        return Response(data,status=status.HTTP_200_OK)



class ShowSingleAuthor(APIView):
    def get(self, request):
        id = request.query_params.get('id')
        author = Author.objects.filter(id=id)
        data = []
        for a in author:
            data.append({
                'full_name': a.full_name,
                'pen_name': a.pen_name,
                'is_alive': a.is_alive,
                'content': a.content,
            })
        return Response(data,status=status.HTTP_200_OK)



class AddToShopcard(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        username = request.user.username
        id = request.data.get('id')

        user = get_object_or_404(User, username=username)
        book = get_object_or_404(Book, id=id)

        user.shopcard.add(book)

        return Response(status=status.HTTP_200_OK)



class RemoveFromShopcard(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        username = request.user.username
        id = request.data.get('id')

        user = get_object_or_404(User, username=username)
        book = get_object_or_404(Book, id=id)

        user.shopcard.remove(book)

        return Response(status=status.HTTP_200_OK)
    


class ShowShopcard(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        username = request.user.username
        users = get_object_or_404(User, username=username)
        books = users.shopcard.all()

        data = []
        for book in books:
            data.append({
                'id': book.id,
                'title': book.title,
                'author': [a.full_name for a in book.author.all()],
                'publisher': [p.full_name for p in book.publisher.all()],
                'translator': [t.full_name for t in book.translator.all()],
                'genre': [g.name for g in book.genre.all()],
                'description': book.description,
                'price': book.price
            })

        total_price = 0
        for prc in data:
            total_price += prc.get('price')

        Number_of_books_in_the_shopcart = len(data)         

        return Response({'status': 'ok', 'data': data, 'total_price': total_price, 'Number_of_books_in_the_shopcart': Number_of_books_in_the_shopcart}, status=status.HTTP_200_OK)



class CreateFactor(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        username = request.user.username
        users = get_object_or_404(User, username=username)

        books = users.shopcard.all()

        data = []
        for book in books:
            data.append({
                'id': book.id,
                'price': book.price
            })

        total_price = 0
        for prc in data:
            total_price += prc.get('price')
    
        GateWay.objects.create(user=users, price=total_price)
        return Response(status=status.HTTP_200_OK)



class PayFactor(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        username = request.user.username
        users = get_object_or_404(User, username=username)
        id = request.data.get('id')

        factor = get_object_or_404(GateWay, id=id)

        if factor.user == users:
            factor.is_paid = True
            factor.save()
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        return Response(status=status.HTTP_200_OK)