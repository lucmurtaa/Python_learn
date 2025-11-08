nota1 = float(input("Digite a primeira nota: "))
while nota1 < 0 or nota1 > 10:
    print(f"A {nota1} inválida. Digite uma nota entre 0 e 10: ", end="")
    nota1 = float(input())

nota2 = float(input("Digite a segunda nota: "))
    
while nota2 < 0 or nota2 > 10:
    print(f"A {nota2} inválida. Digite uma nota entre 0 e 10: ", end="")
    nota2 = float(input())

media = (nota1 + nota2) / 2
print("A média das notas é:", media)