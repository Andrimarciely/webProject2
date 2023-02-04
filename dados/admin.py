from django.contrib import admin
from .models import Parametro, Amostra, FormularioDeAmostra, SolicitacaoDeServico, ListaDeServico

# Register your models here.
admin.site.register(Parametro)
admin.site.register(Amostra)
admin.site.register(FormularioDeAmostra)
admin.site.register(SolicitacaoDeServico)
admin.site.register(ListaDeServico)