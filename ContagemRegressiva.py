# Usuario vai inserir um numero, e o programa faz uma contagem regressiva ate 0

num = int(input("Digite um número: "))
for i in range(num, -1, -1):
    print(i)