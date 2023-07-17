from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import redirect
from flask import flash
from wtforms.csrf.session import SessionCSRF
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask import jsonify
import forms
from wtforms.widgets import html_params
import sqlite3
from sqlite3 import Error



ordenes_MttoBD= r'C:\\Users\\echirino\\Documents\\Proyecto N°1 ordnes mtto\\Mantienimiento SAP\\App_Ordenes_Mtto\\static\\db\\ordenes_Mtto.db'




app = Flask(__name__)
app.secret_key = 'mi_clave'
csrf = SessionCSRF()

#---------------------------------------------------------Ruta del login-----------------------------------------------------------------------------#

@app.route("/", methods = ["GET","POST"])
def login():
        
    titulo = "Inicio_de_sesion"
    login_form = forms.login(request.form)
    
    if request.method == "POST" and login_form.validate():
        #-----declaracion variables-----------#
        username = login_form.username.data.lower()
        clave = login_form.clave.data
        
        #-----conexión con base de datos-------#
        connect=sqlite3.connect(ordenes_MttoBD)
        cursor= connect.cursor()
        sentencia= (""" SELECT username, password from usuarios where username = ?""")
        tabla=cursor.execute(sentencia, (username,))
        tabla=tabla.fetchone()
        connect.commit()
        connect.close()
        try:
            password= tabla[1]
            username= tabla[0]
        except:
            password=None
        if clave == password and username is not None:
            session['user']=username
            return  redirect(url_for ('orden_mantenimiento'))
            
        else:
        
            pass
       
    return render_template("index.html", titulo=titulo,form = login_form)

#---------------------------------------------------------Ruta de orden-----------------------------------------------------------------------------#

@app.route("/orden", methods = ["GET", "POST"])
def orden_mantenimiento():
    
    titulo = "orden_mantenimiento"
    orden_form = forms.orden_mantenimiento(request.form)
    
    #-↓↓ se comentaron estas variables para la futura actualizacion de la app↓↓-#
    #status_form= forms.orden_mantenimiento(request.form)
    #descripcion_orden_form= forms.orden_mantenimiento(request.form)
    
    if request.method== "POST":
        #-------declaracion variables------#
        orden=orden_form.orden.data
        #status=status_form.status.data
        #descripcion= descripcion_orden_form.descripcion_orden.data
        
        #------conexion base de datos-----#
        connect=sqlite3.connect(ordenes_MttoBD)
        cursor= connect.cursor()
        sentencia= (""" INSERT INTO notificacion (orden) VALUES (?)""" )
        cursor.execute(sentencia, (orden,))
        connect.commit()
        connect.close()
        
        
        return redirect(url_for('notificacion', n=orden))
    return render_template("indexformulario.html",titulo=titulo, form=orden_form )
 
 
 
#---------------------------------------------------------Ruta de formulario de notificación-----------------------------------------------------------------------------#
@app.route("/notificacion-<int:n>", methods = ["GET", "POST"])

def notificacion(n):
   
    datos_form= forms.notificacion(request.form)
    titulo= "notificacion"
    puestos_d_trabajo_form = forms.notificacion(request.form)
    ficha_entrada_form= forms.notificacion(request.form)
    tiempoReal_form= forms.notificacion(request.form)
    selecNotificacion_form= forms.notificacion(request.form)
    timeStart_form= forms.notificacion(request.form)
    timeEnd_form= forms.notificacion(request.form)
    texto_forms= forms.notificacion(request.form)
    
    if request.method== "POST":
        #-------declaracion Variables----------#
        ficha_entrada= ficha_entrada_form.ficha_entrada.data
        puestos_d_trabajo=puestos_d_trabajo_form.puestos_d_trabajo.data
        tiempo_real=tiempoReal_form.tiempo_real.data
        selec_notificacion=selecNotificacion_form.selec_notificacion.data
        time_start=timeStart_form.time_start.data
        time_end=timeEnd_form.time_end.data
        texto=texto_forms.texto.data
            
        #--------conexion base de datos----------#
        connect=sqlite3.connect(ordenes_MttoBD)
        cursor= connect.cursor()
        sentencia= (""" UPDATE notificacion 
                        SET tiempo_real=?, fecha_inicio=?, fecha_terminado=?, selec_notificacio=?, textArea=?, puesto_trabajo=?, ficha_entrada=? 
                        WHERE orden=? """ )
        orden=n  
        arg=(tiempo_real,  time_start, time_end, selec_notificacion, texto, puestos_d_trabajo, ficha_entrada, orden)
        cursor.execute( sentencia, arg )
        connect.commit()
        connect.close()
           
        return redirect(url_for('orden_mantenimiento'))
    return render_template("notificacion.html", titulo=titulo, form=datos_form)


#---------------------------------ruta del registro----------------------------------------------------------#
@app.route("/registrar", methods = ["GET", "POST"])
def registrar():
    titulo="registrar"
    registrar_form=forms.registro(request.form)
    nombre_form=forms.registro(request.form)
    apellido_form=forms.registro(request.form)
    username_form=forms.registro(request.form)
    clave_form=forms.registro(request.form)
    nivel_form= forms.registro(request.form)
    ficha_form=forms.registro(request.form)
    
    if request.method== "POST":
    #-------declaracion variables----------#
        nombre=nombre_form.nombre.data.lower()
        apellido=apellido_form.apellido.data.lower()
        username=username_form.username.data
        clave=clave_form.clave.data
        nivel=nivel_form.nivel.data
        ficha=ficha_form.ficha.data
        
        
    #-------Conexion base de datos----------#    
        connect=sqlite3.connect(ordenes_MttoBD)
        cursor= connect.cursor()
        
      
        username=nombre+"_"+apellido
        sentencia= (""" INSERT INTO usuarios (username, password, nombre, apellido, nivel, ficha) VALUES (?,?,?,?,?,?)""" )
        
        titulo=username
        cursor.execute( sentencia, ( username, clave, nombre, apellido, nivel, ficha  ))
        connect.commit()
        connect.close()
        
        return redirect(url_for('login'))
    return render_template("registrar.html",titulo=titulo, form=registrar_form)


    
if __name__ == "__main__":
    
	app.run(debug=True, port=5000, host="0.0.0.0")
        