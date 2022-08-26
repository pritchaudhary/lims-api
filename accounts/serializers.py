from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers, exceptions
from accounts.models import User, UserProfile


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token

    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data


class LoginSerializer(serializers.Serializer):
    # to show textboxes in rest form
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        style={"input_type": "password"}, required=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = User.objects.filter(username=username).last()
        if not user:
            raise serializers.ValidationError(
                "User not exist"
            )
        elif not user.check_password(password):
            raise serializers.ValidationError(
                "Username & Password don't match. Please provide correct details."
            )
        attrs["user"] = user
        return attrs


class UserAccountProfileSerializer(serializers.ModelSerializer):
    contact_number = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    roles = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ("guid", "email", "first_name", "middle_name", "last_name",
                  "name", "contact_number", "roles")

    @staticmethod
    def get_name(obj):
        if obj:
            return f"{obj.first_name} {obj.middle_name} {obj.last_name}"
        return None

    def get_contact_number(self, obj):
        user_id = self.context.get("user_id")
        if obj and obj.user and obj.user.contact_number:
            return obj.user.contact_number
        elif User.objects.filter(id=user_id).exists():
            return User.objects.get(id=user_id).contact_number
        return None

    @staticmethod
    def get_roles(obj):
        if obj and obj.user:
            return obj.user.roles
        return []
