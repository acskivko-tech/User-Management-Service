
from rest_framework import serializers
from auth_app.models import UserModel, Status


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'email','first_name', 'last_name','phone_number','city','status']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self,validated_data):
        user = UserModel(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data.get('phone_number','000-000-0000'),
            city=validated_data.get('city','world'),
            status=validated_data.get('status','-'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
