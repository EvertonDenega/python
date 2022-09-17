
from django.urls import path

from . import views

# Aqui criamos um 'namespace' para as rotas. Assim evitamos caso de conflito de rotas,
# onde o djando não saiba em qual pacote uma rota deve ser carregada.
app_name = "polls"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results", views.results, name="results"),
    path("<int:question_id>/vote", views.vote, name="vote"),
]
