
from rest_framework import serializers
from .models import User, Beverage, SulphiteStatus, BeverageSulphiteStatus

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

        def create(self, validated_data):
            '''
            This method creates a new user
            set_password() hashes the password
            save() saves the user to the database
            '''
            user = User(
                email = validated_data['email'],
                username = validated_data['username']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user

        related_name ='users'

class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beverage
        fields = '__all__'

class SulphiteStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SulphiteStatus
        fields = '__all__'

class BeverageSulphiteStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeverageSulphiteStatus
        fields = '__all__'

class UserBeverageSulphiteStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeverageSulphiteStatus
        fields = '__all__'
        depth = 1