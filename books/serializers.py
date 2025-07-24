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


class GetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    subtitle = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.subtitle = validated_data.get('subtitle', instance.subtitle)
        instance.author = validated_data.get('author', instance.author)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance