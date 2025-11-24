
from rest_framework import serializers
from auth_app.models import UserModel, Status


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = UserModel
        fields = ['username', 'email','first_name', 'last_name','phone_number','city','status','password']

    def create(self,validated_data):
        user = UserModel(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data.get('phone_number','000-000-0000'),
            city=validated_data.get('city','world'),
            status=validated_data.get('status',0),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
