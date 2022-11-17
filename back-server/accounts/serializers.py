from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    pass
    # level = serializers.CharField(max_length=100)

    # def get_cleaned_data(self):
    #     data = super().get_cleaned_data()
    #     data['level'] = self.validated_data.get('level','')
    #     return data
