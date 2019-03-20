from django import forms
from lovelace.models import Usuario
from datetime import date
from lovelace.models import Formulario

#class DateInput(forms.DateInput):
#    input_type = 'date'

class UsuarioCriarForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nome_usuario',
            'dt_nasc_usuario',
            'email_usuario',
            'senha_usuario'
        ]

class FormGuia(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = [
            'iluminado',
            'movimentado',
            'vigilancia',
            'seguranca'
        ]

# class Vota(forms.Form):
#     VOTA=[('iluminado', 'Iluminado?'),
#          ('movimentado','Movimentado'),
#          ('vigilancia', 'Vigilancia'),
#          ('segura', 'Voce se sente segura aqui?')]
         #array com valor e label dos radio buttons

    # vota = forms.MultipleChoiceField(
    #     #criando um objeto do tipo MultipleChoicefield, diferente do RadioSelect. As opções são passadas com parâmetros do próprio objeto, e não do objeto ChecboxSelectMultiple
    #     label='Classifique:',
    #     widget=forms.CheckboxSelectMultiple,
    #     # choices=VOTA
    # )

    outros = forms.CharField(
        max_length=256,
        label='Outros / Deixe sua opinião',
        widget=forms.TextInput(
            attrs={
                'required' : True,
                'id' : 'outros'
            }
        )
    )

class UsuariooCriarForm(forms.Form):
#    foto_usuario = forms.ImageField(
#        label='Foto do Perfil: '
#        widget=forms.ImageField(
#            attrs={
#                'required': True,
#                'id' : 'foto_usuario'
#            }
#        )
#    )

    nome_usuario = forms.CharField(
        max_length=120,
        label='Nome:',
        widget=forms.TextInput(
            attrs={
                'required': True,
                'id' : 'nome_usuario'
            }
        )
    )

    dt_nasc_usuario = forms.DateTimeField(
        label='Data de Nascimento',
        #input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            #format='%d/%m/%Y',
            attrs={
                'required' : True,
                'id' : 'dt_nasc_usuario',
            }
        )
    )

    email_usuario = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(
            attrs={
                'required' : True,
                'id' : 'email_usuario'
            }
        )
    )

    senha_usuario = forms.CharField(
        max_length=30,
        label='Senha',
        widget=forms.TextInput(
            attrs={
                'required' : True,
                'id' : 'senha_usuario'
            }
        )
    )

    confirma_senha_usuario = forms.CharField(
        max_length=30,
        label='Confirme a senha:',
        widget=forms.TextInput(
            attrs={
                'required' : True,
                'id' : 'confirma_senha_usuario'
            }
        )
    )

class ParceirasCriarForm(forms.Form):
#    foto_parceira = forms.ImageField(
#        label='Foto do Perfil: '
#        widget=forms.ImageField(
#           attrs={
#               'required': True,
#               'id' : 'foto_parceira'
#           }
#       )
#    )

    nome_parceira = forms.CharField(
        max_length=120,
        label='Nome:',
        widget=forms.TextInput(
            attrs={
                'required' : True,
                'id' : 'nome_parceira'
            }
        )
    )

    formacao = forms.CharField(
        max_length=60,
        label='Formação',
        widget=forms.TextInput(
            attrs={
                'required' : True,
                'id' : 'formacao'
            }
        )
    )

    profissao = forms.CharField(
        max_length=60,
        label='Profissão',
        widget=forms.TextInput(
            attrs={
                'required' : True,
                'id' : 'profissao'
            }
        )
    )

    endereco_atend = forms.CharField(
        max_length=100,
        label='Endereço',
        widget=forms.TextInput(
            attrs={
                'required' : True,
                'id' : 'endereco_atend'
            }
        )
    )

    CHOICES=[('online', 'Online'),
         ('presencial','Presencial')]
         #array com valor e label dos radio buttons

    tipo_atend = forms.CharField(
        #criando um objeto do tipo RadioSelect passando como parâmetro o array de choices
        label='Tipo de Atendimento',
        widget=forms.RadioSelect(choices=CHOICES)
    )

    valor = forms.CharField(
        max_length=60,
        label='Valor a ser cobrado',
        widget=forms.TextInput(
            attrs={
                'required' : True,
                'id' : 'valor'
            }
        )
    )

    telefone_parceiras = forms.CharField(
        max_length=11,
        label='Telefone',
        widget=forms.TextInput(
            attrs={
                'required' : True,
                'id' : 'telefone_parceiras'
            }
        )
    )

    celular_parceiras= forms.CharField(
        max_length=11,
        label='Celular',
        widget=forms.TextInput(
            attrs={
                'required': True,
                'id' : 'celular_parceiras'
            }
        )
    )

    email_parceiras= forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'required': True,
                'id' : 'email_parceiras'
            }
        )
    )