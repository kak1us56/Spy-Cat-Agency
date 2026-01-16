from rest_framework import viewsets, status, routers
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Cat, Mission, Target
from .serializers import CatSerializer, MissionSerializer, TargetSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def delete(self, request: Request) -> Response:
        mission = self.get_object()
        if mission.cat is not None:
            return Response(
                {"error": "You can not delete the mission set to a cat"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request)


class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    http_method_names = ['get', 'put', 'patch']


router = routers.DefaultRouter()
router.register(prefix=r"cats", viewset=CatViewSet, basename="cats")
router.register(prefix=r"missions", viewset=MissionViewSet, basename="missions")
router.register(prefix=r"targets", viewset=TargetViewSet, basename="targets")
