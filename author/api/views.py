from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import RetrieveDestroyAPIView, DestroyAPIView, UpdateAPIView
from author.api.serializers import AuthorSerializer
from author.models import Account
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class AuthorListAPIView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailAPIView(RetrieveAPIView):

    queryset = Account.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = "href"


class AuthorDeleteAPIView(DestroyAPIView):

    queryset = Account.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = "href"


class AuthorUpdateAPIView(UpdateAPIView):

    queryset = Account.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = "href"


class AuthorCreateAPIView(CreateAPIView):

    queryset = Account.objects.all()
    serializer_class = AuthorSerializer

