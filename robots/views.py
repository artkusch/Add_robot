from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Robot
from .serializers import RoborSerializer


class RobotAPIView(APIView):
    def get(self, request):
        r = Robot.objects.all()
        return Response({'posts': RoborSerializer(r, many=True).data})

    def post(self, request):
        serializer = RoborSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Robot.objects.create(
            model=request.data['model'],
            version=request.data['version'],
            serial=request.data['model'] + '-' + request.data['version'],
            created=request.data['created']
        )

        return Response({'post': RoborSerializer(post_new).data})