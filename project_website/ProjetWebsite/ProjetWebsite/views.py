from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Mundo!!!")

def despedida(request):
    return HttpResponse("Adiós Mundo!!!")

from django.http import HttpResponse

def adulto(request, nombre):
    nombre_letras = len(nombre)  # Aquí se usa len() correctamente
    if nombre_letras:
        return HttpResponse(f"Tu nombre tiene {nombre_letras} letras.")
    else:
        return HttpResponse("No se proporcionó un nombre.")


        


