#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.


#Vamos multiplicar a largura por altura, assim terei a area.

larg = float (input('largura da parede'))
alt = float (input('altura da parede'))
area = larg * alt
print ('sua parede tem a dimensao de {}x{} e sua area é de {}m².'.format(larg, alt, area))

tinta = area /2

print ('para pintar essa parede, voce precisara de {}l de tinta.'.format(tinta))
