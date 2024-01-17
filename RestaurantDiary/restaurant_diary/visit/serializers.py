from rest_framework import serializers
from .models import Visit


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['id', 'user', 'restaurant', 'date_visited', 'expense', 'note', 'rating']

    def create(self, validated_data):
        user = self.context['request'].user
        restaurant = validated_data['restaurant']

        # Check if the user created the restaurant
        if user != restaurant.user:
            raise serializers.ValidationError("You can only create a visit for your own restaurants.")

        visit = Visit.objects.create(user=user, **validated_data)
        return visit
