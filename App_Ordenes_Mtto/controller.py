import sqlite3 

def tabla1():
    connect=sqlite3.connect("ordenes_Mtto.db")
    try:
        cursor= connect.cursor()
        cursor.execute(""" CREATE TABLE usuarios (
            Id integer PRIMARY KEY,
            username VARCHAR(20),
            password VARCHAR(10),
            nombre VARCHAR(10),
            apellido VARCHAR(10),
            nivel integer, 
            ficha integer
            )""")
        print("se creo la tabla usuarios")                        
    except sqlite3.OperationalError:
        print("La tabla articulos 'usuarios' ya existe")      
        connect.commit()
        connect.close()
    connect.close()


        

def tabla2():
    connect=sqlite3.connect('ordenes_Mtto.db')
    try:
        cursor= connect.cursor()
        cursor.execute(""" CREATE TABLE notificacion (
            orden integer(7),
            tiempo_real integer, 
            fecha_inicio VARCHAR(15),
            fecha_terminado VARCHAR(15),
            selec_notificacio VARCHAR(15), 
            textArea text,
            puesto_trabajo text
            )""")
        connect.commit()
        print("se creo la tabla articulos de notificacion")                        
    except sqlite3.OperationalError:
        print("La tabla articulos 'notificacion' ya existe")      
        connect.commit()
        connect.close()
    connect.close()
    
        
tabla1()
tabla2()
