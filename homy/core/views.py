from rest_framework.response import Response
from core.models import Contact
from core.serializers import ContactSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class ContactView(APIView):
  def post(self, request, format=None):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Thankyou For Conatact Us', 'status':'success', 'candidate':serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)
  
  def get(self, request, format=None):
    contact = Contact.objects.all()
    serializer = ContactSerializer(contact, many=True)
    return Response({'status':'success', 'candidates':serializer.data}, status=status.HTTP_200_OK)
