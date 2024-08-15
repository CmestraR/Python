from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Mundo!!!")

def despedida(request):
    return HttpResponse("Adiós Mundo!!!")

def adulto(request, nombre, edad, sexo):

    nombre_letras = nombre.len()
    if nombre_letras:
        return HttpResponse(f"Tu nombre tiene {nombre_letras}")


        


