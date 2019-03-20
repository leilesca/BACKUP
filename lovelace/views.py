#aqui virá toda a lógica da aplicação. Vai extrair as informações da model e entregá-las a um template.

from django.shortcuts import render, redirect
from .forms import FormGuia
# Incluir os modelos/classes (definidos em models.py):
from .models import Usuario, Parceiras, Estabelecimento, Categoria, FiltroParceiras, Formulario

# Create your views here.

def render_index(request):
    return render(request, 'index.html')
    #criada uma função (def) chamada render_index que recebe um parâmetro request, executa a função render que irá renderizar o modelo (banco) de acordo com o template index.html e retorna o resultado
    #request -> tudo que recebemos do usuário através da internet

def render_cadastrousuario(request):
    form = forms.UsuarioCriarForm(request.POST or None)
    form.is_valid()
    return render(request, 'cadastrousuario.html', {'form': form})
    #funçao render que possui o parâmetro request

def salvarusuario(request):
    form = forms.UsuarioCriarForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('/cadastrousuario/')

def render_usuario(request):
    usuario = PerfilUsuario.objects.all()
    return render(request, 'usuario.html', {'dadosusuario' : usuario})

def render_home(request):
    return render(request, 'home.html')

def render_maps(request):
    if request.method == 'POST':
        formulario = FormGuia(request.POST)
        if formulario.is_valid():
                formulario = Formulario()
                formulario.iluminado = request.POST['iluminado']
                formulario.movimentado = request.POST['movimentado']
                formulario.vigilancia = request.POST['vigilancia']
                formulario.seguranca = requests.POST['seguranca']
                formulario.save()
    return render(request, 'maps.html', {'form': Formulario})

def render_guia(request):
    return render(request, 'guia.html')

def render_guiaresultados(request):
    estabelecimentos = Categoria.objects.all()
    return render(request, 'guiaresultados.html', {'items' : estabelecimentos})

def render_guiaresultadosbalada(request):
    estabelecimentos = Categoria.objects.all()
    return render(request, 'guiaresultadosbalada.html', {'items' : estabelecimentos})

def render_guiaresultadosacademia(request):
    estabelecimentos = Categoria.objects.all()
    return render(request, 'guiaresultadosacademia.html', {'items' : estabelecimentos})

def render_guiaresultadosparque(request):
    estabelecimentos = Categoria.objects.all()
    return render(request, 'guiaresultadosparque.html', {'items' : estabelecimentos})

def render_guiaresultadoslazer(request):
    estabelecimentos = Categoria.objects.all()
    return render(request, 'guiaresultadoslazer.html', {'items' : estabelecimentos})

def render_guiaresultadosoutros(request):
    estabelecimentos = Categoria.objects.all()
    return render(request, 'guiaresultadosoutros.html', {'items' : estabelecimentos})

def render_parceiras(request):
    return render(request, 'parceiras.html')
 
def render_parceirasresultados(request):
    parceiras = FiltroParceiras.objects.all()
    return render(request, 'parceirasresultados.html', {'itemsparceiras' : parceiras})

def render_parceirasresultadospersonal(request):
    parceiras = FiltroParceiras.objects.all()
    return render(request, 'parceirasresultadospersonal.html', {'itemsparceiras' : parceiras})

def render_parceirasresultadospsicologa(request):
    parceiras = FiltroParceiras.objects.all()
    return render(request, 'parceirasresultadospsicologa.html', {'itemsparceiras' : parceiras})

def render_cadastroparceiras(request):
    form = forms.ParceirasCriarForm(request.POST or None)
    form.is_valid()
    return render(request, 'cadastroparceiras.html', {'form': form})

def salvarparceiras(request):
    form = forms.ParceirasCriarForm(request.POST or None)
    form.is_valid()
    parceira_obj = Parceiras.objects.create()
    parceira_obj.nome_parceira = request.POST['nome_parceira']
    parceira_obj.formacao = request.POST['formacao']
    parceira_obj.profissao = request.POST['profissao']
    parceira_obj.endereco_atend = request.POST['endereco_atend']
    parceira_obj.tipo_atend = request.POST['tipo_atend']
    parceira_obj.valor = request.POST['valor']
    parceira_obj.telefone_parceiras = request.POST['telefone_parceiras']
    parceira_obj.celular_parceiras = request.POST['celular_parceiras']
    parceira_obj.email_parceiras = request.POST['email_parceiras']
    parceira_obj.save()

    return redirect('/cadastroparceiras/')

def render_forum(request):
    return render(request, 'forum.html')