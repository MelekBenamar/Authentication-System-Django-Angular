from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = User
        fields = ['id','name','email','password'] #specifies the fields that we want

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        
        

# 'extra_kwargs': 

    # allows you to define additional configuration for specific fields.

# 'write_only: True'
 
    # means that the password field will only be used when writing data (e.g., during user creation) but won't be included when retrieving data (like in API responses).

# validated_data.pop('password', None):

    # Removes the password from the validated data dictionary (because it needs special handling).
    # Returns None if the password is not present.

# self.Meta.model(**validated_data):

    #Creates a new instance of the user model with the remaining fields (e.g., name, email).

# instance.set_password(password):

    # Hashes the password using Django's built-in method before saving it to the database.
    # This is essential for security because it prevents storing plain-text passwords.

# instance.save():

    #Saves the user instance to the database.