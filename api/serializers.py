from rest_framework import serializers
from django.contrib.auth.models import User
from catalog.models import Book, Author, Genre



class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='Author.last_name')

    class Meta:
        model = Book
        fields = ['title', 'summary', 'publication_date', 'price', 'amount', 'genre', 'author', 'image', 'author_name']


class AuthorSerializer(serializers.ModelSerializer):
    # full_name = serializers.ReadOnlyField(source='get_full_name')

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        model = Author
        fields = ['get_full_name', 'date_of_birth', 'photo', 'first_name', 'last_name']


class GenreSerializer(serializers.ModelSerializer):
    # genre = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Genre
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']