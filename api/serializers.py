from rest_framework import serializers
from sanctuary.models import Player, Post, Reply, GameData

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    display_name = serializers.CharField(source='user.display_name', read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'
    
class GameDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameData
        fields = '__all__'

