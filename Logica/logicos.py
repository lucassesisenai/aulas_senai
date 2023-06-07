nome = str(input('Digite seu nome:'))
idade = int(input('Qual sua idade:'))
dinheiro = float(input('Tem grana? Digite o valor:'))

if(idade >= 18) and (dinheiro>= 2000):
    print(nome,'Pode tirar carta "15%" em 2x!')
else:
  print(nome,'Não pode tirar carta!')   

