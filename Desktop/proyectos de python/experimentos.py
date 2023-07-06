#ingrese el largo y alto de un triangulo y dibujelo de izquierda a derecha y de derecha a izquierda.
'''

alto = input('lado: ')
largo = input('largo: ')

'''
#numeros impares sumados con signos alternantes.
'''
n = int(input('ingrese numero '))
signo = 0
s = 1
i = 1
c = 1
print(i)
while True:
    if c == n:
        break
    c += 1
    i += 2
    if signo == 0:
        print(- i)
        s -= i
        signo += 1
    else:
        s += i
        print(+ i)
        signo = 0

    
print(s)

'''

#elementos de variables caracteres

'''
i = '
 ___
(*_*)
<) )-
/  \_

'
c = 0
for x in i:
    print(x, end= ' ') 
    print(c, end = ' ')
    c += 1

'''

#generador de graficos

grafico = '''
    10.000|
          |
          |
          |
          |
     1.000|
          |
          |
          |
          |                   
       100|                  
          |
          |
          |
          |
        10| 
          |
          |
          |
          |
          0-----------------------------------------------------------
                            T                   L                 P           
                            A                   L                 O
                            Z                   A                 L
                            O                   V                 E
                            N                   E                 R
                                                R                 A
                                                O'''
a = ''
c = 0
gf = ''
flag = True
for x in grafico:
    a += x
    gf += x
    if x == '|':
        if '100' in a:
            gf += (' ' * 15 ) + '--'
            a = ''
        else:
            gf += (' ' * 14) + '|  |'
    c += 1
print(gf)