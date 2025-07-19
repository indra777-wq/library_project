from rest_framework import serializers
from .models import Book


class BookGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'context', 'author', 'isbn', 'price')

        def validate(self, data):
            title = data.get('title')
            author = data.get('author')

            if title and not title.isalpha():
                raise ValidationError({
                    "status": False,
                    "message": "Kitob sarlavhasi faqat harflardan iborat bo'lishi kerak!"
                })

            if Book.objects.filter(title=title, author=author).exists():
                raise ValidationError({
                    "status": False,
                    "message": "Bunday sarlavha va muallifga ega kitob allaqachon mavjud!"
                })

            return data

        def validate_price(self, price):
            if price <= 0 or price > 9999999999:
                raise ValidationError({
                    "status": False,
                    "message": "Narx noto‘g‘ri kiritilgan!"
                })
            return price
