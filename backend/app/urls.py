from rest_framework import routers


from . import views

router = routers.SimpleRouter()
router.register(r"auth", views.AuthenticationView, basename="auth")
router.register(r'questions', views.QuestionModelViewSet)
router.register(r'choices', views.ChoicesModelViewSet)
urlpatterns = router.urls