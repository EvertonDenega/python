
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404     # Função que vai renderizar o template
from django.urls import reverse

from polls.models import Question, Choice


def index(request):
    # Consulta no banco todas as perguntas, ordenando pela data de publicação (as mais recentes primeiro)
    # Utilizando slice, retorna apenas os  5 primeiros registros
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    # context é o dicionário de contexto que vamos passar para o template
    # Basicamente, podemos acessar os valores desse dicionário referenciando os nomes das chaves no template
    context = {"latest_question_list": latest_question_list}


    # render() é a função que renderiza (carrega) o template e o retorna como uma resposta HTTP
    # O primeiro argumento da função é o objeto de requisição, que é um argumento obrigatório
    # O segundo argumento é o caminho onde está o template. Por padrão, o django procura os templates dentro do
    # pacote atual, em uma pasta chamada templates. Se ele encontra essa pasta, tudo que é colocado depois é considerado
    # como o caminho para carregar o template
    # Por último, podemos passar o dicionário de contexto, dessa maneira podemos passar os valores que carregamos
    # no backend da aplicação para o frontend. Basicamente, referenciamos as chaves do dicionário de contexto como
    # variáveis dentro do template
    return render(request, "polls/index.html", context=context)


def detail(request, question_id):
    # Pegamos o id da pergunta que vem via URL, e carregamos essa pergunta do banco de dados
    # A função get_object_or_404 verifica se o registro que está sendo consultado realmente existe na tabela.
    # Se exister, ele retorna o objeto. Se não, ele retorna uma erro HTTP 404 (Not Found)
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/detail.html", context={"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        # pk = primary key
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "Você deve escolher uma opção válida!"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
