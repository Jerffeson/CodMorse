from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CodMorseSerializer

class CodMorseViewSet(APIView):

    def get(self, request):
        serializer = CodMorseSerializer(data=request.data)
        if serializer.is_valid():
            text = CodMorseSerializer.convert_morse_to_text(attrs=request.data)
            return Response({"data": text}, status=status.HTTP_200_OK)
        else:
            return Response({"error": True, "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
