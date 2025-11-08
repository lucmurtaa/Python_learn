#solicitar ao usirio 10 numero e verificar se eles sao pares ou impares



count = 0
soma = 0
count_pares = 0
while count < 10:

    numero = int(input("Digite um nmero : "))
    if numero % 2 == 0:
        print(f"O nmero {numero} é par.")
        count_pares += 1
    else:
        print(f"O nmero {numero} é ímpar.")

    count += 1
    soma += numero
print(f"A soma dos nmeros digitados é: {soma}")

print(f"O total de nmeros pares digitados é: {count_pares}")
print(f"O total de nmeros ímpares digitados é: {10 - count_pares}")
print("Fim do programa.")
