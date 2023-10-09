print("Eres para mi lo que haskell para tecla")
import os
import sys
# Definición de automata
estados_nfa = {
    #Estado inicial
    'q0': { "'": {'q1'},'"': {'q2'},'Number': {'q3'},'symbol': {'q7'},
           #Puede tratarse de PR
           'a': {'q8'},'e': {'q9'}, 'f': {'q10'}, 'm': {'q11'}, 'i': {'q12'},
           'n': {'q13'}, 'p': {'q14'}, 'r': {'q15'}, 't': {'q16'},'v': {'q17'},
           'w': {'q18'},'o': {'q25'}," ": {'q0',},"any": {'q500',} 
        },
    
    #Palabras reservadas
    'q8': {'n': {'q19'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}}, 
    'q19': {'d': {'q20'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}}, 
    'q20': {"symbol": {'q0'},"'": {'q1'},'"': {'q2'}," ": {'q0'},'any': {'q500'}}, #AND
    
    'q9': {'l': {'q21'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q21': {'s': {'q22'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q22': {'e': {'q23'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q23': {"symbol": {'q0'},"'": {'q1'},'"': {'q2'}," ": {'q0'},'any': {'q500'}}, #ELSE Y FALSE y TRUE Y WHILE
    
    'q10': {'a': {'q24'},'o': {'q25'},'u': {'q27'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},#FA o FO
    'q24': {'l': {'q21'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},#Retorna a q21 si todo va bien
    'q25': {'r': {'q26'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q26': {"symbol": {'q7'},"'": {'q1'},'"': {'q2'}," ": {'q0'},'any': {'q500'}}, #FOR y OR Y VAR
    
    'q27': {'n': {'q28'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q28': {"symbol": {'q0'},"'": {'q1'},'"': {'q2'}," ": {'q0'},'any': {'q500'}}, #FUN y RETURN
    
    'q12': {'f': {'q29'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q29': {"symbol": {'q0'},"'": {'q1'},'"': {'q2'}," ": {'q0'},'any': {'q500'}}, #IF
    
    'q13': {'u': {'q30'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q30': {'l': {'q31'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q31': {'l': {'q32'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q32': {"symbol": {'q0'},"'": {'q1'},'"': {'q2'}," ": {'q0'},'any': {'q500'}}, #NULL
    
    'q14': {'r': {'q33'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q33': {'i': {'q34'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q34': {'n': {'q35'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q35': {'t': {'q36'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q36': {"symbol": {'q0'},"'": {'q1'},'"': {'q2'}," ": {'q0'},'any': {'q500'}}, #PRINT
    
    'q15': {'e': {'q37'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q37': {'t': {'q38'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q38': {'u': {'q39'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q39': {'r': {'q28'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},#mandamos a q28 pues termina en n
    
    'q16': {'r': {'q40'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q40': {'u': {'q41'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q41': {'e': {'q23'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},#mandamos a q23 pues termina en e
    
    'q17': {'a': {'q42'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q42': {'r': {'q26'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},#mandamos a q26 pues termina en r
    
    'q18': {'h': {'q43'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q43': {'i': {'q44'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q44': {'l': {'q45'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},
    'q45': {'e': {'q23'}, "symbol": {'q0'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}},#mandamos a q23 pues termina en e
    
    
    #Cadenas
    'q1': {'any': {'q2'}, "'": {'q0'}},
    'q2': {'any': {'q2'}, '"': {'q0'}},
    
    #Numeros
    'q3': {'Number': {'q3'}, "^": {'q4'}, ".": {'q5'},"symbol": {'q7'}," ": {'q0'}, "any": {'q500'},   "'": {'q0'},'"': {'q0'}},#Entero
    'q4': {'Number': {'q4'}, " ": {'q0'}, "symbol": {'q7'},"'": {'q0'},'"': {'q0'}, "any": {'q500'}},#Exponenciales
    'q5': {'Number': {'q5'}, " ": {'q0'}, "symbol": {'q7'},"'": {'q0'},'"': {'q0'}, "any": {'q500'}},#Decimales
    
    #Simbolos , empezamos en q60
    'q7': {'symbol': {'q60'}, " ": {'q0'},"'": {'q0'},'"': {'q0'},'Number': {'q3'},
           'a': {'q8'},'e': {'q9'}, 'f': {'q10'}, 'm': {'q11'}, 'i': {'q12'},
           'n': {'q13'}, 'p': {'q14'}, 'r': {'q15'}, 't': {'q16'},'v': {'q17'},
           'w': {'q18'},'o': {'q25'},
           'any': {'q500'}},
    'q60': {},#Si se llega a q60, se hace siempre una comparacion de que simbolo fue el anterior. Y se sacan conclusiones. Cso 1,2,3,4,5,6
    
    #Identificadores en 500
    'q500': {'symbol': {'q7'},"'": {'q0'},'"': {'q0'}," ": {'q0'},'any': {'q500'}}
}

# Diccionario de simbolos a reconocer
simbolos = ["<", ">", "!", "=", "+", "-", "*", "/", "{", "}", "(", ")", ",", ".", ";"]
#Diccionario de palabras a reconocer
palabras_reservadas=["and","else","false","for","fun","if","null","or","print","return","true","var","while"]
#Diccionario de letras a reconocer
PosiblesPR=["a", "e", "f", "h", "i", "l", "o", "p", "r", "s", "t", "u", "v" ,"w","n"]
#Vocabulario=["a","e","f","i","n","o","p","r","t","v","w","<", ">", "!", "=", "+", "-", "*", "/", "{", "}", "(", ")", ",", ".", ";"]

#Estados Finales PR
estados_FPR=["q20","q23","q26","q28","q29","q32","q36"]
#Estados FINALES para String
estados_FString=["q1","q2"]

# Definición de diccionario de simbolos
nombres_simbolos = {
    '<': 'MENOR_QUE', # se trata del simbolo <
    '>': 'MAYOR_QUE', # se trata del simbolo >
    '!': 'BANG', # se trata del simbolo !
    '=': 'IGUAL', # se trata del simbolo =
    '<=': 'MENOR_IGUAL_QUE', # se trata del simbolo <=
    '>=': 'MAYOR_IGUAL_QUE', # se trata del simbolo >=
    '!=': 'DIFERENTE_QUE', # se trata del simbolo !=
    '==': 'IGUAL_IGUAL', # se trata del simbolo ==
    '+': 'SUMA', # se trata del simbolo +
    '-': 'RESTA', # se trata del simbolo -
    '*': 'ESTRELLA', # se trata del simbolo *
    '{': 'LLAVE_ABRE', # se trata del simbolo {
    '}': 'LLAVE_CIERRA', # se trata del simbolo }
    '(': 'PARENTESIS_ABRE', # se trata del simbolo (
    ')': 'PARENTESIS_CIERRA', # se trata del simbolo )
    ',': 'COMA', # se trata del simbolo ,
    '.': 'PUNTO', # se trata del simbolo .
    ';': 'PUNTO_Y_COMA', # se trata del simbolo ;
    '/': 'SLASH' # se trata del simbolo /
}

class MisTokens:
    def __init__(self, tipo, valor1, valor2):
        self.tipo = tipo
        self.valor1 = valor1
        self.valor2 = valor2

# Lista para almacenar objetos
lista_objetos = []

def evaluar_simbolo(caracter, simbolos):#Esta evaluador me dira si la letra de entrada pertenece al diccionario de simbolos por reconocer
    if caracter in simbolos:
        return "symbol"
    else:
        return None  # El carácter no es un símbolo

def evaluar_numero(caracter):#Esta evaluador me dira si la letra de entrada pertenece al diccionario de numeros por reconocer
    if caracter.isdigit():
        return "Number"
    else:
        return None  # Opcional: puedes devolver None si el carácter no es un dígito

def evaluar_caracter_any(caracter):
    if caracter == '"' or caracter == "'":
        return caracter
    else:
        return "any"


def interprete(caracter, simbolos,PosiblesPR,guardar_como_any):
    if caracter in simbolos:
        return "symbol"
    elif caracter.isdigit():
        return "Number"
    elif caracter == '"' or caracter == "'":
        return caracter
    else:
        if guardar_como_any==1:
            return "any"
        elif caracter==" ":
            print("Caso vacio")
            return caracter
        else:
            return caracter
            #if (caracter in PosiblesPR):
                #return caracter
            #else:
                #return "any"
def analizar_codigo2(codigo):
    print("Se manda a archivo.txt")
    
