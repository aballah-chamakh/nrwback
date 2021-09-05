from rest_framework import serializers
from .models import User,Profile






class UserSerializer(serializers.ModelSerializer):
    #image = serializers.CharField(source='image.url',read_only=True)
    password = serializers.CharField(style={'input_type':'password'},write_only=True,required=True)
    confirmPassword = serializers.CharField(style={'input_type':'password'},write_only=True,required=True)
    class Meta : 
        model = User 
        fields = ('id','email','username','password','confirmPassword')
    def validate(self,data):
        email = data.get('email')
        qs = User.objects.filter(email=email)
        if qs :
            raise serializers.ValidationError('email already exist')
        pw1 = data.get('password')
        pw2 = data.get('confirmPassword')
        # chech if the two password match
        if pw1 != pw2 :
            raise serializers.ValidationError('Passwords should match')
        return data

    def create(self,validated_data):
        password = validated_data.get('password')
        del validated_data['password']
        del validated_data['confirmPassword']
        user_obj = User(**validated_data)
        user_obj.set_password(password)
        user_obj.save()
        return user_obj




class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="user.id")
    username = serializers.CharField(source="user.username")
    email = serializers.CharField(source="user.email")
    image = serializers.CharField(source="image.url")
    class Meta : 
        model = AdminProfile
        fields = ('user_id','slug','username','image','email')

