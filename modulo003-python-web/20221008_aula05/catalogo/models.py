import uuid

from django.db import models
from django.urls import reverse


class Genero(models.Model):

    # help_text é o texto que aparece no admin do django
    nome = models.CharField(max_length=50, help_text="Informe um gênero literário (Ficção, terror, etc)")

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tb_generos'


class Livro(models.Model):

    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    sumario = models.TextField(max_length=100, help_text="Informe uma breve descrição do livro")
    isbn = models.CharField("ISBN", max_length=13, help_text="Informe o ISBN (13 caracteres")
    genero = models.ManyToManyField(Genero, help_text="Informe um gênero para esse livro")

    # este método será usado para mostrar o engero associado ao livro.
    def mostrar_genero(self):
        # retorna uma string com a lista dos generos que estão associados a esse livro.
        return ', '.join([genero.nome for genero in self.genero.all()])

    # short_description será o nome da coluna onde estes generos serão listados.
    mostrar_genero.short_description = "Gênero(s)"

    def __str__(self):
        return self.titulo

    def get_absolut_url(self):
        return reverse('detalhe-livro', args=[str(self.id)])

    class Meta:
        db_table = 'tb_livros'

class CopiaLivro(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID da cópia")
    livro = models.ForeignKey(Livro, on_delete=models.RESTRICT, null=True)
    impressao = models.CharField(max_length=200)
    devolucao = models.DateField(null=True, blank=True)

    STATUS_COPIA = (
        ('m', 'Manutenção'),
        ('e', 'Emprestado'),
        ('d', 'Disponível'),
        ('r', 'Reservado'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS_COPIA,
        blank=True,
        default= 'm',
        help_text="Disponibilidade da cópia"
    )

    def __str__(self):
        return f'{self.id} ({self.livro.titulo})'

    class Meta:
        db_table = 'tb_copias'
        ordering = ['devolucao']


class Autor(models.Model):

    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=200)
    data_de_nascimento = models.DateField("Nascimento \u2605", null=True, blank=True)
    data_de_falecimento = models.DateField("Falecimento \u271F", null=True, blank=True)

    def __str__(self):
        return f'{self.sobrenome}, {self.nome}'

    def get_absolut_url(self):
        return reverse('detalhe-autor', args=[str(self.id)])

    class Meta:
        ordering = ['sobrenome', 'nome']
