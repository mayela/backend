from rest_framework import serializers
from .models import Resource
from userauth.serializers import UserSerializer
from tagging.serializers import TagSerializer, TagsSerializerField



class ResourceSerializer(TagSerializer, serializers.ModelSerializer):

    tags = TagsSerializerField(model_field='tags', default='')
    media_type = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Resource
        lookup_field = 'guid'

        fields = (
            'guid',
            'author',
            'title',
            'description',
            'url',
            'referring_url',
            'other_referring_source',
            'user',
            'date_published',
            'created',
            'modified',
            'media_type',
            'paid',
            'tags'
        )


    def get_media_type(self, obj):
        return obj.get_media_type_display()

