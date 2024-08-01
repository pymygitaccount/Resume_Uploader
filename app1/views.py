from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Profile
from .serializers import ProfileSerializers


class ProfileView(APIView):
  
  def post(self, request, format=None):
    serializer = ProfileSerializers(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'msg':'Resume Uploaded Successfully', 'status':'success', 'profile_data':serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, format=None):
    candidate = Profile.objects.all()
    print('candidate >> ', candidate)
    serializer = ProfileSerializers(candidate, many=True)
    return Response(serializer.data)
    # return Response({'status':'success', 'profile_data':serializer.data}, status=status.HTTP_200_OK)


#########################################
# Test code for Git.


def sum_func(x, y):
  return x + y

sum_func(10, 20)

def mul_func(x, y):
  return x * y

mul_func(2, 6)
