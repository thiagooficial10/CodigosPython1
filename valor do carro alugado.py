dias = int (input('Quantos dias o carro foi alugado?'))
km = float (input('Quantos km foram rodados? '))
pago = (dias * 60) + (km * 0.15)
print('o total a pagar é de R${:.2f}'.format(pago))
