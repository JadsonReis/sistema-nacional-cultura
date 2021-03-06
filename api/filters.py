from django.db.models import Q

from django_filters import rest_framework as filters
from django_filters import Filter

from planotrabalho.models import PlanoTrabalho
from planotrabalho.models import ConselhoCultural
from adesao.models import Municipio
from planotrabalho.models import SituacoesArquivoPlano

class MunicipioFilter(filters.FilterSet):

    estado_sigla = filters.CharFilter(field_name='estado__sigla', lookup_expr='iexact')
    nome_uf = filters.CharFilter(field_name='estado__nome_uf', lookup_expr='iexact')
    nome_municipio = filters.CharFilter(field_name='cidade__nome_municipio', lookup_expr='iexact')
    situacao_adesao = filters.CharFilter(field_name='usuario__estado_processo',
                                         lookup_expr='istartswith')
    data_adesao = filters.DateFilter(field_name='usuario__data_publicacao_acordo')
    data_adesao_min = filters.DateFilter(field_name='usuario__data_publicacao_acordo', lookup_expr=('gte'))
    data_adesao_max = filters.DateFilter(field_name='usuario__data_publicacao_acordo', lookup_expr=('lte'))
    municipal = filters.BooleanFilter(method='municipal_filter')
    estadual = filters.BooleanFilter(method='estadual_filter')
    ente_federado = filters.CharFilter(method='ente_federado_filter')

    situacao_conselho_id = filters.ModelMultipleChoiceFilter(queryset=SituacoesArquivoPlano.objects.all(),
        field_name='usuario__plano_trabalho__conselho_cultural__situacao')
    situacao_orgao_id = filters.ModelMultipleChoiceFilter(queryset=SituacoesArquivoPlano.objects.all(),
        field_name='usuario__plano_trabalho__orgao_gestor__situacao')
    situacao_lei_id = filters.ModelMultipleChoiceFilter(queryset=SituacoesArquivoPlano.objects.all(), 
        field_name='usuario__plano_trabalho__criacao_sistema__situacao')
    situacao_fundo_id = filters.ModelMultipleChoiceFilter(queryset=SituacoesArquivoPlano.objects.all(),
        field_name='usuario__plano_trabalho__fundo_cultura__situacao')
    situacao_plano_id = filters.ModelMultipleChoiceFilter(queryset=SituacoesArquivoPlano.objects.all(),
        field_name='usuario__plano_trabalho__plano_cultura__situacao')

    situacao_conselho_descricao = filters.CharFilter(field_name='usuario__plano_trabalho__conselho_cultural__situacao__descricao',
                                                     lookup_expr='istartswith')
    situacao_orgao_descricao = filters.CharFilter(field_name='usuario__plano_trabalho__orgao_gestor__situacao__descricao',
                                                  lookup_expr='istartswith')
    situacao_lei_descricao = filters.CharFilter(field_name='usuario__plano_trabalho__criacao_sistema__situacao__descricao',
                                                lookup_expr='istartswith')
    situacao_fundo_descricao = filters.CharFilter(field_name='usuario__plano_trabalho__fundo_cultura__situacao__descricao',
                                                  lookup_expr='istartswith')
    situacao_plano_descricao = filters.CharFilter(field_name='usuario__plano_trabalho__plano_cultura__situacao__descricao',
                                                  lookup_expr='istartswith')

    def ente_federado_filter(self, queryset, name, value):

        return queryset.filter(
                Q(estado__sigla__istartswith=value) |
                Q(estado__nome_uf__istartswith=value) |
                Q(cidade__nome_municipio__istartswith=value))

    def estadual_filter(self, queryset, name, value):

        return queryset.filter(cidade__isnull=value)

    def municipal_filter(self, queryset, name, value):
        isnull = not value

        return queryset.filter(cidade__isnull=isnull)

    class Meta:
        model = Municipio
        fields = ('id', 'cnpj_prefeitura', 'data_adesao',
                  'data_adesao_min', 'data_adesao_max')


class PlanoTrabalhoFilter(filters.FilterSet):
    situacao_conselho_id = filters.NumberFilter(field_name='conselho_cultural__situacao__id')
    situacao_conselho_descricao = filters.CharFilter(field_name='conselho_cultural__situacao__descricao',
                                                     lookup_expr='istartswith')

    situacao_orgao_id = filters.NumberFilter(field_name='orgao_gestor__situacao__id')
    situacao_orgao_descricao = filters.CharFilter(field_name='orgao_gestor__situacao__descricao',
                                                  lookup_expr='istartswith')

    situacao_lei_id = filters.NumberFilter(field_name='criacao_sistema__situacao__id')
    situacao_lei_descricao = filters.CharFilter(field_name='criacao_sistema__situacao__descricao',
                                                lookup_expr='istartswith')

    situacao_fundo_id = filters.NumberFilter(field_name='fundo_cultura__situacao__id')
    situacao_fundo_descricao = filters.CharFilter(field_name='fundo_cultura__situacao__descricao',
                                                  lookup_expr='istartswith')

    situacao_plano_id = filters.NumberFilter(field_name='plano_cultura__situacao__id')
    situacao_plano_descricao = filters.CharFilter(field_name='plano_cultura__situacao__descricao',
                                                  lookup_expr='istartswith')

    class Meta:
        model = PlanoTrabalho
        fields = ('id',)