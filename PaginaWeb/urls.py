from django.urls import path
from PaginaWeb.views import PaginaWeb, crear_login, busqueda

urlpatterns = [
     path("", PaginaWeb, name="Pagina Web"),
     path("Login/crear/", crear_login, name = "Login"),
     path("Usuarios/", busqueda, name = "Login"),
]
