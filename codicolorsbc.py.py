
eleccio = int(input('Vols passar de colors a números(1) o de números a colors(2):'))   
listcolors = ['negre','marró', 'vermell', 'taronja','groc', 'verd', 'blau', 'lila', 'gris', 'blanc' ]

if eleccio == 1: #colors a números
    primercolor = str(input('Quin és el primer color?:'))
    segoncolor = str(input('Quin és el segon color?:'))
    tercercolor = str(input('Quin és color tercer color?:'))
    quartcolor= str(input('Quin és color quart color(or o plata)?:'))
    poscol1 = listcolors.index(primercolor)
    poscol2 = listcolors.index(segoncolor)
    poscol3 = (10) ** listcolors.index(tercercolor)
    if quartcolor == 'or':
        poscol4 = '5%'
    elif quartcolor == 'plata':
        poscol4 = '10%'
    
    numfin = int(str(poscol1) + str(poscol2)) * poscol3
    print('Els ohms de la resistència són:',numfin,'i la tolerància és de:', poscol4)

if eleccio == 2: #números a colors
    numero = list(input('ohms de la resistència?:'))

    numerolenght = len(numero)
    num1 = numero[0]
    num2 = numero[1]
    color1 = listcolors[int(num1)]
    color2 = listcolors[int(num2)]
    color3 = listcolors[(int(numerolenght) - 2)]

    print('Els colors són: ' + color1 , color2 , color3 )
