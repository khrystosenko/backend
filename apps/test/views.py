from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class TestView(APIView):
    """
    Test view that requires auth token
    """

    permission_classes = (IsAuthenticated,)
    def get(self, request):
        return Response({'msg': 'It does work, fo\' shizzle my nizzle.'})
