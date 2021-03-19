from rest_framework import permissions, views, response


class HealthAPIView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return response.Response({'message': 'success'})
