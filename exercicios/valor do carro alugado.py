--Pede ao usuário para digitar quantos dias o carro foi alugado. O valor é convertido para inteiro e armazenado na variável dias.
--Pede ao usuário para informar quantos quilômetros foram rodados. O valor é convertido para número decimal (float) e armazenado na variável km.
--Calcula o valor total a pagar:
R$ 60,00 por cada dia alugado
R$ 0,15 por cada quilômetro rodado

--Mostra o valor total com duas casas decimais.*/

dias = int (input('Quantos dias o carro foi alugado?'))
km = float (input('Quantos km foram rodados? '))
pago = (dias * 60) + (km * 0.15)
print('o total a pagar é de R${:.2f}'.format(pago))
