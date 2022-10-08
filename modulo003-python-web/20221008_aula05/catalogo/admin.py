from django.contrib import admin

from .models import Genero, Livro, CopiaLivro, Autor


class AutorAdmin(admin.ModelAdmin):
    list_display = ('sobrenome', 'nome', 'data_de_nascimento', 'data_de_falecimento')


class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'mostrar_genero')



admin.site.register(Genero)
admin.site.register(Livro, LivroAdmin)
admin.site.register(CopiaLivro)
admin.site.register(Autor, AutorAdmin)



