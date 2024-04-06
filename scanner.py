# Archivo generado automáticamente por el programa de instalación de la aplicación
import pickle
import sys

TOKENS = {0: ' return WHITESPACE ', 1: ' return ID ', 2: ' return NUMBER ', 3: ' return PLUS ', 4: ' return MINUS ', 5: ' return TIMES ', 6: ' return DIV ', 7: ' return LPAREN ', 8: ' return RPAREN '}

def print_tokens():
    return TOKENS

def simular_afd2(afd, cadena):
    estado_actual = afd.get_estado_inicial()
    cadena_aceptada = False
    estado_aceptado = []
    # print(estado_actual.id)
    cadena_leida = ''
    while len(cadena) > 0:
        for char in cadena:
            # print(char)
            estado_siguiente = estado_actual.get_trancisiones(char)
            if estado_siguiente:
                cadena_leida += char
                estado_actual = estado_siguiente[0]
                # print(estado_actual.id)
                if estado_actual.es_final:
                    estado_aceptado.append([estado_actual, cadena_leida])
            else:
                if estado_aceptado != []:
                    token_encontrado = estado_aceptado.pop()
                    print(token_encontrado[1], token_encontrado[0].token)

                    cadena = cadena[len(token_encontrado[1]):]
                    estado_actual = afd.get_estado_inicial()
                    cadena_leida = ''
                    estado_aceptado = []
                    break
                else:
                    cadena_leida += char
                    print(cadena_leida, 'Lexema no encontrado')
                    cadena = cadena[len(cadena_leida):]
                    estado_actual = afd.get_estado_inicial()
                    cadena_leida = ''
                    break
        if estado_aceptado != []:
            token_encontrado = estado_aceptado.pop()
            print(token_encontrado[1], token_encontrado[0].token)
            break

def main():
    with open('afd.pickle', 'rb') as f:
        afd = pickle.load(f)
    if len(sys.argv) == 2:
        try:
            with open(sys.argv[1], 'r') as f:
                validacion = f.read()
        except:
            print('Archivo no encontrado')
            exit()
    else:
        print('No se ha ingresado los parametros correctos')
        exit()
    
    simular_afd2(afd, validacion)

if __name__ == '__main__':
    main()