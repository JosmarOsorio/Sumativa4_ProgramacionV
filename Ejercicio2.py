import qrcode  #Importamos la biblioteca qrcode para generar códigos QR

def generar_codigo_qr(url, tamaño, color_fondo, color_codificacion): #Creamos una funcion para generar el código QR con la URL proporcionada
    codigo_qr = qrcode.QRCode(
        box_size=tamaño,  #Establecemos el tamaño de cada caja del código QR
        border=4,  #Establecemos el tamaño del borde del código QR
    )
    codigo_qr.add_data(url)  #Agregamos la URL al código QR
    codigo_qr.make(fit=True)  #Generamos el código QR

    imagen_qr = codigo_qr.make_image(fill_color=color_codificacion, back_color=color_fondo) #Creamos la imagen del código QR teniendo en cuenta los colores ingresador por el usuario

    return imagen_qr

url_python = "https://www.python.org" #Establcemos el url que le vamos a agregar al QR
tamaño_qr = int(input("Ingresa el tamaño del código QR (Ejemplo: 10): "))  #Mostramos un mensaje solicitando al usuario el tamaño del código QR
color_fondo_qr = input("Ingresa el color de fondo del código QR (Solo ingrese nombres de colores en ingles por favor): ")  #Mostramos un mensaje solicitando al usuario el color de fondo
color_codificacion_qr = input("Ingresa el color de codificación del código QR (Solo ingrese nombres de colores en ingles por favor): ") #Mostramos un mensaje solicitando al usuario el color de codificación

qr_personalizado = generar_codigo_qr(url_python, tamaño_qr, color_fondo_qr, color_codificacion_qr) #Generamos el código QR usando la funcion generar codigo QR


nombre_archivo = "codigo_qr_personalizado.png" #Establecemos el nombre con el que vamos a guardar la imagen del QR
qr_personalizado.save(nombre_archivo) #Guardamos el QR con el nombre establcedio anteriormente 

print("¡Código QR personalizado generado y guardado en", nombre_archivo, "!") #Mostramos un mensaje diciendo que se ha guardado con exito el QR