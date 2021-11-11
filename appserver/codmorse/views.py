from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CodMorseSerializer

class CodMorseViewSet(APIView):

    def get(self, request):
        print(request.GET['codMorseParam'])
        serializer = CodMorseSerializer(data={'codMorseParam': request.GET['codMorseParam']})
        if serializer.is_valid():
            text = CodMorseSerializer.convert_morse_to_text(request.GET['codMorseParam'])
            return Response({"data": text}, status=status.HTTP_200_OK)
        else:
            return Response({"error": True, "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
