from rest_framework import serializers
from .models import user as User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    #extra_kwargs = {'password':{'write_only':True,'required':True}}