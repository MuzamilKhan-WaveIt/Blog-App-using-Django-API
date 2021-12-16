from rest_framework import serializers
from Posts.models import Model

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Model
        fields = ('id', 'title', 'author', 'body', 'created_at', 'updated_at')
