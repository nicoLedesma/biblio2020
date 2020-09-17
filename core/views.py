from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import MateriaLectura



# Create your views here.


class HomeView(TemplateView):
    template_name = 'core/home.html'

    '''
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        msgs = ['Hola', 'te', 'como', 'va?']
        context['msgs'] = msgs
        return context
    '''

# Todos ejemplos de renderizar templates.
from django.template import Template, Context

def obj_template():
    t = Template("<h1>Mi nombre es {{ name }}.</h1>")
    c = Context({'name': 'Nicolas'})
    return print(t.render(c))


def template_1():
    t = Template("El item 2 es {{ items.2 }}")
    c = Context({'items': ['apples', 'bananas', 'carrots']})
    return print(t.render(c))

def template2():
    person = {'name': 'Nicolas', 'age': '43'}
    t = Template("{{ person.name.upper}} is {{ person.age }} years old.")
    c = Context({'person': person})
    return print(t.render(c))

import datetime
from django.template.loader import get_template
from django.http import HttpResponse


def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('core/current_datetime.html') #debe existir este html en la carpeta template, get_template encuentra
                                              # el archivo y devuelve un Objeto Template compilado
    html = t.render({'current_time': now})
    return HttpResponse(html)


from django.shortcuts import render, render_to_response


def current_datetime1():
    now = datetime.datetime.now()
    return render_to_response('core/current_datetime.html', {'current_time': now, 'name': 'Pablito'}) #deprecated

#estas es la buena!!
def current_datetime2(request):
    now = datetime.datetime.now()
    libro = MateriaLectura.objects.get(id=1) #consulta a la basede datos: select * from MaterialLectura where id =1
    return render(request, 'core/current_datetime.html', {'current_time': now, 'name': request.user, 'libro': libro.titulo})

