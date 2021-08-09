from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse

from stores.models import Pizzeria, Image

UserModel = get_user_model()

class PizzeriaListSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField() ## позволяет применять методы и возвращать данные

    class Meta:
        model = Pizzeria
        fields = (
            'id',
            'pizzeria_name',
            'city',
            'zip_code',
            'absolute_url' ## добавляем к полям
        )

    ## обязателен метод с префиксом get_ и именем поля
    def get_absolute_url(self, obj):
        return reverse('pizzeria_detail', args=(obj.pk, ))


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'image_title', 'upload_at')


class PizzeriaDetailSerializer(serializers.ModelSerializer):
    update = serializers.SerializerMethodField()
    delete = serializers.SerializerMethodField()
    pizzeria_images = ImageSerializer(many=True, required=False)
    
    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'pizzeria_name',
            'street',
            'city',
            'state',
            'zip_code',
            'website',
            'phone_number',
            'description',
            'email',
            'active',
            'update',
            'delete',
            'pizzeria_images',
            'logo_image',
        ]

    def get_update(self, obj):
        return reverse('pizzeria_update', args=(obj.pk, ))
    
    def get_delete(self, obj):
        return reverse('pizzeria_destroy', args=(obj.pk, ))


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        new_token = Token.objects.create(user=user)
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

