from django.contrib import admin

# Register your models here.
from .models import Mensagem
from .models import Categoria
from .models import Tag

@admin.register(Categoria)                                       
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Tag)                                            
class TagAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ("titulo", "criada_em","categoria")
    list_filter = ("categoria","tags")  
    search_fields = ("titulo", "conteudo")
    filter_horizontal = ("tags",)