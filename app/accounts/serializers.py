from django.forms import CharField
from rest_framework import serializers
from .models import User  # Permission, Role, UserRole
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.models import Group, Permission, ContentType
from django.utils.text import slugify
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    email = serializers.EmailField(allow_blank=False)
    # username = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "profile_image",
            # "username",
            "password",
            "is_deleted",
            "is_verified",
            "created_at",
            "updated_at",
        ]

    # def get_username(self, instance):
    #     return slugify(instance.firstname+"_"instance.lastname)

    # def validate_username(self, username):
    #     is_already_exists = User.objects.filter(username=username).exists()
    #     if is_already_exists:
    #         if not username.isalnum():
    #             raise serializers.ValidationError(
    #                 "The username should only contain alphanumerics characters"
    #             )
    #         raise serializers.ValidationError("Username already exists")
    #     return username

    def validate_email(self, email):
        is_already_exists = User.objects.filter(email=email).exists()
        if is_already_exists:
            raise serializers.ValidationError("Email already exists")
        return email

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserUpdateSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField()
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone_number",
            "profile_image",
            "created_at",
            "updated_at",
        ]
    def validate_email(self, email):
        is_already_exists = User.objects.filter(email=email).exists()
        if is_already_exists:
            raise serializers.ValidationError("Email already exists")
        return email


class PasswordResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.password = validated_data.get("password", instance.password)
        instance.save()
        return instance

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ReactivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["is_deleted"]

    def update(self, instance, validated_data):
        instance.is_deleted = validated_data.get("is_deleted", instance.is_deleted)
        instance.save()
        return instance


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {"bad_token": ("Token is expired or invalid")}

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail("bad_token")


class RoleSerializer(serializers.ModelSerializer):
    name = CharField(max_length=100, validators=[UniqueValidator(queryset=Group.objects.all())])
    class Meta:
        model = Group
        fields = "__all__"


class AddUserRoleSerializer(serializers.Serializer):
    class Meta:
        fields = ["user", "role"]


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "phone_number",
        ]
