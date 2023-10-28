#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

# :.2F  ----------> significa formatar em 2 casas decimais flutuantes.

real = float(input('digite quanto dinheiro voce tem na carteira: R$'))
dolar = real / 3.27
print('Com R${:.2f} voce pode comprar ${:.2f} dolares'.format(real,dolar))
