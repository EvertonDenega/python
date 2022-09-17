
from django.urls import path

from . import views

# Aqui criamos um 'namespace' para as rotas. Assim evitamos caso de conflito de rotas,
# onde o djando não saiba em qual pacote uma rota deve ser carregada.
app_name = "store"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:item_list_id>/detail", views.detail, name="detail"),

]
