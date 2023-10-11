# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

algo = input('Digite algo:')

print('O tipo primitivo desse valor é: ', type(algo))
print('So tem espaços?', algo.isspace())
print('E um numero ?', algo.isnumeric())
print('E alfabetico? ',algo.isalpha())
print('E alfanumerico? ',algo.isalnum())
print('E capitalizada', algo.istitle())