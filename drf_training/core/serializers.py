from rest_framework import serializers
from .models import Author, Book, User


class ModelBookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.name", read_only=True)

    class Meta:
        model = Book
        fields = ["id", "title", "published_date", "author", "author_name"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return Book.objects.create(**validated_data)


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=128)
    published_date = serializers.DateField()
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    author_name = serializers.CharField(source="author.name", read_only=True)

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.published_date = validated_data.get(
            "published_date", instance.published_date
        )
        instance.author = validated_data.get("author", instance.author)
        instance.save()
        return instance


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    birth_date = serializers.DateField()
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.birth_date = validated_data.get("birth_date", instance.birth_date)
        instance.save()
        return instance
