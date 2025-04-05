from app.models import Question, Choice
from app.serializers import QuestionSerializer, ChoiceSerializer

from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, mixins, permissions, status
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response

from .models import CustomUser
from .serializers import (
    UserSerializer
)


@permission_classes((permissions.IsAuthenticated,))
class UserViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    @action(methods=["get"], detail=False)
    def current(self, request):
        return Response(
            {
                "current_user": str(request.user),
                "username": request.user.username,
            }
        )


@permission_classes((permissions.AllowAny,))
class AuthenticationView(viewsets.ViewSet):
    @csrf_exempt
    @action(methods=["post"], url_path="login", detail=False)
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            first_login = not user.last_login
            auth.login(request, user)
            username = user.username
            return Response(
                {
                    "user": {"username": username},
                    "firstLogin": first_login,
                }
            )

    @action(methods=["post"], url_path="logout", detail=False)
    def logout(self, request):
        if request.user.is_authenticated:
            auth.logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes((permissions.AllowAny,))
class QuestionModelViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    class Meta:
        model = Question


@permission_classes((permissions.AllowAny,))
class ChoicesModelViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    class Meta:
        model = Choice
