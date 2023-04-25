from rest_framework import serializers

from interview.inventory.models import UserProfile, UserRoles


class OrderTagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderTag
        fields = ['id', 'name', 'is_active']

class OrderTagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderTag
        fields = ['id', 'name', 'is_active']
class OrderTagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderTag
        fields = ['id', 'name', 'is_active']


class ProfilesSerializer(serializers.ModelSerializer):
    user_ = User()
    language = InventoryLanguageSerializer()
    tags = InventoryTagSerializer(many=True)
    metadata = serializers.JSONField()
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user_name', 'email', 'password', 'first_name', 'last_name', 'avatar']
