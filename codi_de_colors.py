print("""
****************************************************************************************
Aquest és un exercici per a practicar el codi de colors de les resistències.

RECORDA - FACTORS DE MULTIPLICACIÓ

NEGRE = x1   MARRÓ = x10   VERMELL = x100   TARONJA = x1000

GROC = x10000   VERD = x100000   BLAU = x1000000

RECORDA - FACTORS DE TOLERÀNCIA

OR = +-5%
PLATA = +-10%
CAP VALOR = +-20%

FUNCIONAMENT:
En la primera pregunta podem decidir passar un codi de colors al valor de la resistència
(colors) o passar del valor de la resistència al codi de colors(numero)

****************************************************************************************
"""
)

RESPOSTA = input("""
Introdueix la paraula "numero" per a passar d'un valor numèric a codi de colors.
Introdueix la paraula "colors" per a passar un codi de colors a un valor numèric.

RESPOSTA: """)
if RESPOSTA == "colors":
    
    ## Preguntar valors i validar-los

    color1 = input("Color1: ")
    color2 = input("Color2: ")
    color3 = input("Color3: ")
    Tolerancia = input("Tolerancia: ")
    
    ## Definir valors en minúscules perquè no hi hagin problemes

    color1 = color1.lower()
    color2 = color2.lower()
    color3 = color3.lower()
    Tolerancia = Tolerancia.lower()

    ## Variable de color primera fila

    if color1 == "marro" or "marró":
        color1_final = 1
    if color1 == "vermell":
        color1_final = 2
    if color1 == "taronja":
        color1_final = 3
    if color1 == "groc":
        color1_final = 4
    if color1 == "verd":
        color1_final = 5
    if color1 == "blau":
        color1_final = 6
    if color1 == "lila":
        color1_final = 7
    if color1 == "gris":
        color1_final = 8
    if color1 == "blanc":
        color1_final = 9
    if color1 == "negre":
        color1_final = 0
        
    ## Variable de colors segona fila

    if color1 == "marro" or "marró":
        color2_final = 1
    if color2 == "vermell":
        color2_final = 2
    if color2 == "taronja":
        color2_final = 3
    if color2 == "groc":
        color2_final = 4
    if color2 == "verd":
        color2_final = 5
    if color2 == "blau":
        color2_final = 6
    if color2 == "lila":
        color2_final = 7
    if color2 == "gris":
        color2_final = 8
    if color2 == "blanc":
        color2_final = 9
    if color2 == "negre":
        color2_final = 0
        
    ## Variable de colors tercera fila

    if color3 == "marro" or "marró":
        color3_final = 10
    if color3 == "vermell":
        color3_final = 100
    if color3 == "taronja":
        color3_final = 1000
    if color3 == "groc":
        color3_final = 10000
    if color3 == "verd":
        color3_final = 100000
    if color3 == "blau":
        color3_final = 1000000
    if color3 == "lila":
        color3_final = 1
    if color3 == "negre":
        color3_final = 1

    ## Definir la tolerància

    if Tolerancia == "or":
        tolerancia_final = "+-5%"
    if Tolerancia == "plata":
        tolerancia_final ="+-10%"
    if Tolerancia == "":
        tolerancia_final = "+-20%"

    ## Multiplicació de valors

    Resistencia_1 = int(color2_final) * int(color3_final)
    Resistencia_2 = [int(a) for a in str(Resistencia_1)]

    ## Determinar si posas Kohms, Mohms o Ohms

    if len(Resistencia_2) == 7:
        Resistencia_1 = Resistencia_1 / 1000000
        signe = "MΩ"
        print(f"Resistència = {color1_final}{Resistencia_1} {signe} amb un {tolerancia_final} de tolerància!")
    if len(Resistencia_2) == 6:
        Resistencia_1 = Resistencia_1 / 100000
        Lletra1 = str(Resistencia_1)
        Lletra1_final = Lletra1[0]
        print(Lletra1_final)
        signe = "MΩ"
        print(f"Resistència = {color1_final}.{Lletra1_final} {signe} amb un {tolerancia_final} de tolerància!")
    if len(Resistencia_2) == 5:
        Resistencia_1 = Resistencia_1 / 1000
        signe = "KΩ"
        print(f"Resistència = {color1_final}{Resistencia_1} {signe} amb un {tolerancia_final} de tolerància!")
    if len(Resistencia_2) == 4:
        Resistencia_1 = Resistencia_1 / 1000
        signe = "KΩ"
        print(f"Resistència = {color1_final}{Resistencia_1} {signe} amb un {tolerancia_final} de tolerància!")
    if len(Resistencia_2) == 3:
        Resistencia_1 = Resistencia_1 / 100
        Lletra1 = str(Resistencia_1)
        Lletra1_final = Lletra1[0]
        signe = "KΩ"
        print(f"Resistència = {color1_final}.{Lletra1_final} {signe} amb un {tolerancia_final} de tolerància!")
    if len(Resistencia_2) == 2:
        Resistencia_1 = Resistencia_1
        signe = "Ω"
        print(f"Resistència = {color1_final}{Resistencia_1} {signe} amb un {tolerancia_final} de tolerància!")
    if len(Resistencia_2) == 1:
        Resistencia_1 = Resistencia_1
        signe = "Ω"
        print(f"Resistència = {color1_final}{Resistencia_1} {signe} amb un {tolerancia_final} de tolerància!")
    
if RESPOSTA == "numero":
    numero = int(input("Numero: "))
    
    ## Definir color primera fila

    number_2 = [int(a) for a in str(numero)]
    if len(number_2) == 1:
        print("Valor incorrecte. La resistència ha de ser major a 9 Ohms") 
        exit()
    if len(number_2) >= 9:
        print("Has introduit un valor massa gran. EL límit són 8 dígits!")
    if number_2[0] == 0:
        numero_fila1 = "negre"
    if number_2[0] == 1:
        numero_fila1 = "marró"
    if number_2[0] == 2:
        numero_fila1 = "vermell"
    if number_2[0] == 3:
        numero_fila1 = "taronja"
    if number_2[0] == 4:
        numero_fila1 = "groc"
    if number_2[0] == 5:
        numero_fila1 = "verd"
    if number_2[0] == 6:
        numero_fila1 = "blau"
    if number_2[0] == 7:
        numero_fila1 = "lila"
    if number_2[0] == 8:
        numero_fila1 = "gris"
    if number_2[0] == 9:
        numero_fila1 = "blanc"

    ## Definir color segona fila

    if number_2[1] == 0:
        numero_fila2 = "negre"
    if number_2[1] == 1:
        numero_fila2 = "marró"
    if number_2[1] == 2:
        numero_fila2 = "vermell"
    if number_2[1] == 3:
        numero_fila2 = "taronja"
    if number_2[1] == 4:
        numero_fila2 = "groc"
    if number_2[1] == 5:
        numero_fila2 = "verd"
    if number_2[1] == 6:
        numero_fila2 = "blau"
    if number_2[1] == 7:
        numero_fila2 = "lila"
    if number_2[1] == 8:
        numero_fila2 = "gris"
    if number_2[1] == 9:
        numero_fila2 = "blanc"

    ## Definir color tercera fila

    numero = [int(a) for a in str(numero)]
    numero.pop(0)
    numero.pop(0)
    
    if len(numero) == 6:
        numero_fila3 = "blau"
    if len(numero) == 5:
        numero_fila3 = "verd"
    if len(numero) == 4:
        numero_fila3 = "groc"
    if len(numero) == 3:
        numero_fila3 = "taronja"
    if len(numero) == 2:
        numero_fila3 = "vermell"
    if len(numero) == 1:
        numero_fila3 = "marró"
    if len(numero) == 0:
        numero_fila3 = "negre"

    numero_fila1 = numero_fila1.upper()
    numero_fila2 = numero_fila2.upper()
    numero_fila3 = numero_fila3.upper()

    print(f"El codi de colors de la teva resistència és: {numero_fila1} | {numero_fila2} | {numero_fila3}")