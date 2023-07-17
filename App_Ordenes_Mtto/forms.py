from wtforms import Form
from wtforms import StringField
from wtforms import IntegerField
from wtforms import PasswordField
from wtforms import RadioField
from wtforms import SelectField

from wtforms import validators
from wtforms import IntegerField
from wtforms import FloatField, DecimalField
from wtforms import BooleanField
from wtforms.fields import TimeField
from wtforms.fields import DateField
from wtforms import HiddenField
from wtforms import SubmitField
from wtforms.fields import BooleanField
from wtforms.fields.html5 import DateTimeLocalField 
from wtforms.fields import TextAreaField
from wtforms.fields import DateTimeField, TimeField






def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo no debe estar vacio.')

class login(Form):
    username = StringField("", [validators.InputRequired(message="Nombre de usuario vacio!")])
    clave = PasswordField("", [validators.InputRequired(message="Ingrese la contraseña!"),
                               validators.Length(min=6,max=15,message="Se requiere contraseña")])
    honeypot = HiddenField('',[length_honeypot])
    
    
class orden_mantenimiento(Form):
    orden=IntegerField("", [validators.InputRequired(message="rellene este campo!"),
                               validators.Length(max=7)])
    
    #status=StringField("", )
    #descripcion_orden=StringField("", )
    
    
class notificacion(Form):
     ficha_entrada = IntegerField("",)
     puestos_d_trabajo = SelectField('', choices=[('Electricista', 'Electricista'), ('Mecánico', 'Mecánico'), ('Supervisor', 'Supervisor'), ('Servicios Generales', 'Servicios Generales')])
     tiempo_real = IntegerField("", [validators.input_required(message="Ingrese los datos en el campo soicitado")])
     selec_notificacion = SelectField('', choices=[('Notificación final', 'Notificación final'), ('Sin trabajo rest', 'Sin trabajo rest'), ('Trabajo rest', 'Trabajo rest')])
     time_start=  DateTimeLocalField("", format='%Y-%m-%dT%H:%M')
     time_end=  DateTimeLocalField("",  format='%Y-%m-%dT%H:%M')
     texto= TextAreaField("",)
     id= IntegerField("",)
     
     
class registro(Form):
    username = StringField("", [validators.InputRequired(message="Nombre de usuario vacio!")])
    clave = PasswordField("", [validators.InputRequired(message="Ingrese la contraseña!"),
                               validators.Length(min=6,max=15,message="Se requiere contraseña")])
    nombre= StringField("", [validators.InputRequired(message="Nombre de usuario vacio!")])
    apellido= StringField("", [validators.InputRequired(message="Nombre de usuario vacio!")])
    nivel= IntegerField("", [validators.input_required(message="Ingrese los datos en el campo soicitado"),
                             validators.Length(min=6,max=15)])
    ficha = IntegerField("", [validators.InputRequired(message="Nombre de usuario vacio!")])