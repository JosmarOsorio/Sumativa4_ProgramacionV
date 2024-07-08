#Programar en Python un generador de contraseñas aleatorio. Por: Josmar osorio. Para: Programación V-UBA

import random #importamos la funcion random

def generar_contrasena(longitud): #Definicmos la funcion generar contraseña con el parametro de la logniguitud que se vaya a ingresar
    caracteres = "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890/*-+!" #Creamos una varibale que contenga los caracteres que podria contener la contraseña 
    contraseña = "" #Creamos una avriable contraseña que irá almacenando los caracteres iterados de la misma
    for i in range(longitud): #Creamos un ciclo for que itere y agregue caracteresa  la contraseña segun la longitud ingresada por el usuario
        contraseña += random.choice(caracteres) #utiizamos random para que escoja un caracter aleatoriamente de la variable caracteres y la guarde en la variable contraseña
    return contraseña 

longitud_deseada = int(input("Ingresa la longitud deseada para la contraseña: ")) #Mostramos un mensaje por pnatalla pidiendole al usiario la longitud deseada de la contraseña a generar

contraseña_generada = generar_contrasena(longitud_deseada) #llamamos a la funcion generar contraseña para mostar la contraseña generada mediante la variable contraseña generada

print("La contraseña generada es:", contraseña_generada) #Mostramos por pnatalla un mensaje con la contraseña generada
