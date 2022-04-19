from enum import Enum, auto

import re

#Esta clase contiene los enum para manejar los diferentes tipos de elementos del lenguaje
class TipoComponente(Enum):
    COMENTARIO = auto()
    PALABRA_CLAVE = auto()
    CONDICIONAL = auto()
    REPETICION = auto()
    ASIGNACION = auto()
    OPERADOR = auto()
    COMPARADOR = auto()
    TEXTO = auto()
    IDENTIFICADOR = auto()
    ENTERO = auto()
    FLOTANTE = auto()
    BOOLEAN = auto()
    PUNTUACION = auto()
    BLANCOS = auto()
    NINGUNO = auto()
    FUNCION = auto()
    CUERPO = auto()
    RECORRER = auto()
    DEVOLVER = auto()


class ComponenteLéxico:
    tipo    : TipoComponente
    texto   : str

    def __init__(self, tipo_nuevo: TipoComponente, texto_nuevo: str):
        self.tipo = tipo_nuevo
        self.texto = texto_nuevo

    def __str__(self):
        resultado = f'{self.tipo:30} <{self.texto}>'
        return resultado

class Explorador:

    descriptores_componentes  = [(TipoComponente.COMENTARIO, r'^chok:'),
                               (TipoComponente.CONDICIONAL, r'^(eta)'),
                               (TipoComponente.REPETICION, r'^(amauk)'),
                               (TipoComponente.ASIGNACION, r'^(dor)'),
                               (TipoComponente.FUNCION, r'^(del)'),
                               (TipoComponente.CUERPO, r'^(kewe|bata)'),
                               (TipoComponente.DEVOLVER, r'^(dokmale)'),
                               (TipoComponente.RECORRER, r'^(ie|e)'),
                               (TipoComponente.OPERADOR, r'^(ukotkok|shok|balatok|berie)'),
                               (TipoComponente.COMPARADOR, r'^(tse|kibi|btaie|kuoki)'),
                               (TipoComponente.TEXTO, r'^(~.?[^~])~'),
                               (TipoComponente.IDENTIFICADOR, r'^([a-z][a-zA-Z0-9_]+)'),
                                (TipoComponente.ENTERO, r'^(-?[0-9]+)'),
                               (TipoComponente.FLOTANTE, r'^(-?[0-9]+.[0-9]+)'),
                               (TipoComponente.BOOLEAN, r'^(chokale|kocho)'),
                                (TipoComponente.PUNTUACION, r'^([,{}()])'),
                                (TipoComponente.BLANCOS, r'^(\s)')]

    # Constructor de la clase
    def __init__(self, contenido_archivo):
        self.texto = contenido_archivo
        self.componentes = []

    # Recorre todas las palabras del archivo de texto
    def explorar(self):
        for linea in self.texto:
            resultado = self.procesar_linea(linea)
            self.componentes = self.componentes + resultado

    # Imprime los elementos
    def imprimir_componentes(self):
        for componente in self.componentes:
            print(componente)

    # Recorre el txt buscando los elementos lexicos
    def procesar_linea(self, linea):
        componentes = []
        while(linea !=  ""):
            for tipo_componente, regex in self.descriptores_componentes:
                respuesta = re.match(regex, linea)
                if respuesta is not None :
                    if tipo_componente is not TipoComponente.BLANCOS and \
                            tipo_componente is not TipoComponente.COMENTARIO:

                        nuevo_componente = ComponenteLéxico(tipo_componente, respuesta.group())
                        componentes.append(nuevo_componente)

                    linea = linea[respuesta.end():]
                    break;

        return componentes