###### Exercício 1

idade_usuario = int(input("Digite a sua idade para a verificação do voto: "))

if idade_usuario < 16:
    print("Não pode votar.")
    print()

elif (idade_usuario>=16 and idade_usuario<18) or (idade_usuario>=70):
    print("O voto é opcional.")
    print()

else:
    print("O voto é obrigatorio")
    print()

######## Exercício 2

ler_num = int(input("Digite o número para a verificação: "))

if ler_num % 2==0:
    print()
    print("O número é par.")

else:
    print()
    print("O número é ímpar.")
    print()

######## Exercício 3

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print()
if num1>num2:
    print("O primeiro número é maior.")
    print()

elif num2==num1:
    print("Os números são iguais.")
    print()

else:
    print("O segundo número é maior.")
    print()

######## Exercício 4

n1 = float(input("Digite a sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))
n3 = float(input("Digite a sua terceira nota: "))
n4 = float(input("Digite a sua quarta nota: "))

cm = (n1 + n2 + n3 + n4) / 4
print("A sua media final é:", cm) 
print("Então: ")


if cm >= 7:
    print("Você foi aprovado!")
    print()

elif cm>=5 and cm<=7:
    print("Você está de recuperação.")
    print()

else:
    print("Você esta reprovado.")
    print()

######## Exercício 5

vA = int(input("Digite o primeiro valor: "))
vB = int(input("Digite o segundo valor: "))

if vA % vB == 0 or vB % vA == 0:
    print("São múltiplos")
    print()
else:
    print("Não são múltiplos")
    print()

######## Exercício 6

def calculadora(nu1, nu2, char):
    if char == '+':
        return nu1 + nu2
    elif char == '-':
        return nu1 - nu2
    elif char == '*':
        return nu1 * nu2
    elif char == '/':
        if nu2 or nu1 == 0:
            return "Erro: divisão por zero!"
        return nu1 / nu2
    else:
        return "Erro: operação inválida!"

nu1 = int(input("Digite o primeiro número: "))
nu2 = int(input("Digite o segundo número: "))
char = (input("Digite a operação desejada para o cálculo (+, -, / ou *): "))

conta = calculadora(nu1, nu2, char)

print(f"Conta: {nu1} {char} {nu2} = Resultado: {conta}")
print()

######## Exercício 7

anoat = 2026

anonas = int(input("Digite a sua data de nascimento: "))
idade = anoat - anonas

if idade>=18:
    print(f"Com: {idade} anos, o voto é obrigatório!")
    print()

elif (idade>=16 and idade<18) or idade>=70:
    print(f"Com: {idade} anos, o voto é opcional este ano.")
    print()

else:
    print(f"Com: {idade} anos, o voto é proibido este ano:")
    print()

######## Exercício 8

salario = float(input("Digite o seu salário: R$"))

if salario<=280:
    aumento = salario * (20 / 100)
    percentual = ("20%")
    salariof = salario + aumento

elif salario>280 and salario<700:
    aumento = salario * (15 / 100)
    percentual = ("15%")
    salariof = salario + aumento

elif salario>700 and salario<1500:
    aumento = salario * (10 / 100)
    percentual = ("10%")
    salariof = salario + aumento

else:
    aumento = salario * (5 / 100)
    percentual = ("5%")
    salariof = salario + aumento

print(f"Salário antes do ajuste: R$", salario)
print(f"O percentual de aumento aplicado:", percentual)
print(f"O valor do aumento será de: R$", round(aumento, 2))
print(f"O salário final será de: R$", round(salariof, 2))
print()

######## Exercício 9

estado = int(input("Digite o código do estado de origem (1 a 5): "))
peso = float(input("Digite o peso da carga (em toneladas): "))
codigo_carga = int(input("Digite o código da carga (10 a 40): "))

kg = round(peso * 1000,2)

if codigo_carga>=10 and codigo_carga<=20:
    preco = 100

elif codigo_carga >= 21 and codigo_carga <= 30:
    preco = 250
    preco = 250

else:
    preco = 340

preco_carga = kg * preco

if estado==1:
    taxa_imposto = 0.35

elif estado==2:
    taxa_imposto = 0.25

elif estado ==3:
    taxa_imposto = 0.15

elif estado==4:
    taxa_imposto = 0.05

else:
    taxa_imposto = 0

imposto = preco_carga * taxa_imposto
total = preco_carga + imposto

print(f"O peso da carga do caminhão convertido em quilos é de:", kg, "kg")
print(f"O Preço da carga é de: R$ {round(preco_carga, 2)}")
print(f"Imposto ({taxa_imposto*100}%): R$ {round(imposto, 2)}")
print(f"Total transportado: R$ {round(total, 2)}")

######## Exercício 10

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if a > b:
    a, b = b, a
if c > a:
    a, c = c, a

if c > b:
    b, c = c, b

print(f"A = {a}, B = {b}, C = {c}")

if a >= b+c:
    print("NAO FORMA TRIANGULO")

elif a==b or b==c or c==a:
    print("TRIANGULO ISOSCELES")

elif a==b and b==c and c==a:
    print("TRIANGULO EQUILATERO")

elif a**2 == b**2 + c**2:
    print("TRIANGULO RETANGULO")

elif a**2 > b**2 + c**2:
     print("TRIANGULO OBTUSANGULO")

elif  a**2 < b**2 + c**2:
    print("TRIANGULO ACUTANGULO")


print ("FIM")