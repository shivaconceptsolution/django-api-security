from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import MyData
from .serializers import MyDataSerializer

class InsertDataView(APIView):
    authentication_classes = [TokenAuthentication]  # Token-based authentication
    permission_classes = [IsAuthenticated]          # Requires authentication
    
    def post(self, request):
        serializer = MyDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)