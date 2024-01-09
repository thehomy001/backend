from rest_framework import serializers
from core.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'f_name', 'l_name', 'email', 'phone_number', 'message']