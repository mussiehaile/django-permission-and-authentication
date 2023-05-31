from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, TokenSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'username', 'password','is_active','is_superuser','is_staff','is_director','is_vice_director']
