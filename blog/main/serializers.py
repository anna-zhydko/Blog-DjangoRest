from rest_framework import serializers
from .models import Post, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    # category_title = serializers.CharField(source='category.title')
    # category = serializers.HyperlinkedRelatedField(
    #     queryset=Category.objects.all(),
    #     lookup_field='title',
    #     view_name='category-detail'
    # )
    # category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    # category_title = serializers.RelatedField(source='category.title', read_only=True)

    # category_parent = serializers.HyperlinkedRelatedField(view_name='category-detail', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(PostSerializer, self).to_representation(instance)
        rep['category'] = instance.category.title
        # rep['user']
        return rep
