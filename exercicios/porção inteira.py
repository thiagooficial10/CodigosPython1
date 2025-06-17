import math
num = float (input('Digite um valor:' ))
print ('O valor digitado foi {} e a sua porção é {}'.format(num, math.trunc(num))) 
#metodo math.trunc mostra a porcao inteira do numero


#ou podemos utilizar outra função sem importar biblioteca

num = float (input('Digite um valor: '))
print ('O valor digitado e {} e a sua porção inteira é {}'.format(num, int(num)))
