#Desafio 1
#1 - Perguntar a idade do usuario e guardar em uma variavel
#2 - Exibir a idade na tela

idade = int(input('Qual a sua idade? '))
print('Você tem {} '.format(idade))

#Desafio 2
#1 - Perguntar as notas dos cinco alunos e guardar em variáveis
#2 - Somar as notas através de variáveis e calcular a média delas
#3 - Exibir a média aritmética das notas na tela

nota1 = float(input('Qual a nota do primeiro aluno? '))
nota2 = float(input('Qual a nota do segundo aluno? '))
nota3 = float(input('Qual a nota do terceiro aluno? '))
nota4 = float(input('Qual a nota do quarto aluno? '))
nota5 = float(input('Qual a nota do quinto aluno? '))
media = (nota1+nota2+nota3+nota4+nota5)/5
print('A média dos 5 alunos é {}'.format(media))

#Desafio 3
#1 - O Programa terá uma lista com nomes de times armazenados nela
#2 - O Programa exibirá os nomes dos times na tela

times = ['Flamengo, Cruzeiro, Coritiba, Santa Cruz, Sport']
print(times)

#Desafio 4
#1 - O Programa pergunta a idade da pessoa
#2 - O Programa confere se a idade é maior ou igual a 18
    #2.1 - Se sim, exibe na tela que o usuário é maior de idade
    #2.2 - Se não, exibe na tela que o usuário é menor de idade

idade2 = int(input('Qual a sua idade? '))
if idade2 >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')

#Desafio 5
#1 - O Programa solicita um número
#2 - O Programa analisa o número e descobre se ele é divisível ou não por 2
    #2.1 - Se sim, exibe que o número que o usuário digitou é par
    #2.2 - Se não, exibe que o número que o usuário digitou é ímpar

numerodiv = int(input('Digite um número: '))
if numerodiv % 2 == 0:
    print('O Número {} é par'.format(numerodiv))
else:
    print('O número {} é ímpar'.format(numerodiv))

#Desafio 6
#1 - O programa perguntará um número ao usuário
#2 - O programa irá calcular se o número é divível por si mesmo
    #2.1 - Se sim, exibe na tela que o número é primo
    #2.2 - Se não, exibe na tela que o número não é primo

numerop = int(input('Digite um número: '))
if numerop % 2 == 0:
    print('O Número não é primo')
elif numerop  % 3 == 0:
    print('O Número não é primo')
elif numerop % 5 == 0:
    print('O Número não é primo')
elif numerop % 7 == 0:
    print('O Número não é primo')
else:
    print('O número é primo')
