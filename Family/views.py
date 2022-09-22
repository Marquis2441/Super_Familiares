from django.shortcuts import render
from django.template import Template, context, loader
from Family.models import SuperFamiliares

def listar_Family(request):
    queryset = SuperFamiliares.objects.all()
    diccionario = {'Family': queryset}
    plantilla = loader.get_template('Family_list.html')
    documento_html = plantilla.render(diccionario)

    return HttpResponse(documento_html)
