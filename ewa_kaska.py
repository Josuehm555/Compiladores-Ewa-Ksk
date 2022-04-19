#Archivo Principal
from utils import archivos as utils
from explorador.explorador import Explorador

import argparse

parser = argparse.ArgumentParser(description='Interprete para Ewa Kaska')

parser.add_argument('--solo-explorar', dest='explorador', action='store_true', 
        help='Explora')

parser.add_argument('archivo',
        help='Archivo de código fuente')

def ewaKaska():

    args = parser.parse_args()

    if args.explorador is True: 

        texto = utils.cargar_archivo(args.archivo)

        exp = Explorador(texto)
        exp.explorar()
        exp.imprimir_componentes()

    elif args.python is True:

        texto = utils.cargar_archivo(args.archivo)

        exp = Explorador(texto)
        exp.explorar()


    else:
        parser.print_help()


if __name__ == '__main__':
    ewaKaska()
