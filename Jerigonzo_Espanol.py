import pyphen
from variables import *

def jerigonzo_a_silaba(silaba:str)->str:
    if len(silaba) == 0:
        return ""
    elif len(silaba) == 1 and silaba in consonantes:
        return silaba
    elif len(silaba) == 2:
        return ""
    else:
        return jerigonzo_a_silaba(silaba[:-1]) + silaba[-1]
    
def jeringozo_a_espanol(palabra:str)->str:
    separador = pyphen.Pyphen(lang="es")
    silabas = separador.inserted(palabra).split("-")
    for i in range(len(silabas)):
        if i%2:
            silabas[i] = jerigonzo_a_silaba(silabas[i])
    palabra = "".join(silabas)
    return palabra