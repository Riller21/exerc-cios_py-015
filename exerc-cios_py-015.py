# Criar vetor
numeros = []


# Loop solicita a inserção dos números.
for _ in range(10):
    numero = int(input("Insira um número: "))
    
    numeros.append(numero)

# Variavel retorna que para cana numero em numeros eleva-se ao quadrado e soma todo resultado da potencia.
resultado = sum(x ** 2 for x in numeros)

print(f"A soma dos quadrados de cada número digitado é: {resultado}")