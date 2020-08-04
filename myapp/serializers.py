from rest_framework import serializers
from .models import Profile, Address
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    # profile = ProfileSerializer(required=True)
    class Meta():
        model = User
        fields = ('username','email','password',)

        extra_kwargs = {
        'password':{'write_only':True},
        }
    
    def get(self, request):
        pass

    def create(self, validated_data):
        user = User.objects.create(**validated_data
            # username=validated_data['username'],
            # email=validated_data['email'],
            # password=validated_data['password'],
            # # profile = validated_data['profile'],
        )
        # profile_data = validated_data.pop('profile')
        # profile = Profile.objects.create(
        #     user = user
        #     # gender = profile_data['gender'],
        #     profile_pic = profile_data['profile_pic'],


        # )
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)

class AddressSerializer(serializers.ModelSerializer):

    class Meta():
        model = Address
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta():
        model = Profile
        fields = ('user','phone_number','gender','date_of_birth','friends')

        # password = Profile.user.password

    def create(self, validated_data):
        # self.user.create(**validated_data)
        profile = Profile.objects.create_user(**validated_data)
        return profile

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password=validated_data.pop(password)
            isinstance.set_password(password)
        return super(ProfileSerializer, self).update(instance, validated_data)
