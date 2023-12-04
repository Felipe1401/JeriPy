import pyphen
from variables import *

def silaba_a_jerigonzo(silaba:str)->str:
    if len(silaba) == 0:
        return ""
    if len(silaba) == 1 and silaba in consonantes:
        return silaba
    if silaba[-1].lower() in vocales:
        return silaba + "p" + silaba[-1]
    return silaba_a_jerigonzo(silaba[:-1]) + silaba[-1]

def espanol_a_jeringozo(palabra:str)->str:
    separador = pyphen.Pyphen(lang="es")
    silabas = separador.inserted(palabra).split("-")
    for i in range(len(silabas)):
        silabas[i] = silaba_a_jerigonzo(silabas[i])
    palabra = "".join(silabas)
    return palabra