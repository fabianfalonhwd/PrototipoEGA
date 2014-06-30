from django.forms import ModelForm
from django import forms
from apps.home.models import Carrera, Materia, MesaFinal, InscripcionMateria, InscripcionFinal, HistorialAcademico
from apps.alumno.models import User

class CarreraForm(ModelForm):


	class Meta:

		model = Carrera
		fields = ('cod_carrera', 'nombre', 'resolucion', 'duracion')


	cod_carrera = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese el codigo de la carrera',
					'required' : 'required'
				}))

	nombre = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese nombre de la carrera',
					
				}))

	resolucion = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese numero de resolucion de la carrera',
					
				}))

class MateriaForm(ModelForm):


	class Meta:

		model = Materia
		fields = ('cod_materia','nombre', 'carrera', 'duracion')


	cod_materia = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese el codigo de la materia',
					'required' : 'required'
				}))

	nombre = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'Ingrese nombre de la Materia',
					
				}))

class UserForm(ModelForm):

	class Meta:

		model = User
		fields = ('nombre_apellido', 'username','email', 'cod_alumno', 'dni', 'lugar_nacimiento',
					'fecha_nacimiento', 'ciudad_actual', 'domicilio_actual','tipo_usuario',
					'documentacion_completa','imagen', 'password')





class HistorialForm(ModelForm):

	class Meta:

		model = HistorialAcademico


class MesaFinalForm(ModelForm):

	class Meta:

		model = MesaFinal

		



