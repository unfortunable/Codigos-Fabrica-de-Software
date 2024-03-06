from rest_framework_routers import default_routers
from viewsets import PessoasViewSet
from django.urls import include, path
router = default_routers

rooter.register("pessoa",PessoasViewSet)

urlspatterns = [
    path("api",include)
] 