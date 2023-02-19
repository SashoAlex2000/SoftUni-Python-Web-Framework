from rest_framework import serializers

from sample_rest_api.api_todos.models import Todo, Category


class TodoForListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id', 'title'
        )


class TodoForCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id', 'title', 'description', 'category'
        )

    def create(self, validated_data): # override the 'create' functionality to add the user
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id', 'name'
        )
        model = Category


class TodoForDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id', 'title', 'description', 'is_done'
        )



