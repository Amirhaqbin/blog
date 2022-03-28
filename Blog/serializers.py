from .models import Post, Comment
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'author',
            'body',
            'status'    
    )
        extra_kwargs = {'author' : {'required' : False}}

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'post',
            'id',
            'user',
            'text',
            'rating'
        )

    read_only_fields = ('user', 'id')

    def create(self, validated_data):
        user = self.context['user']
        validated_data["user"] = user
        instance = super().create(validated_data)
        return instance