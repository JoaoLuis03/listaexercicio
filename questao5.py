numeros = [7, 5, 8, 20, 12, 1, 18]
soma_pares = 0
contagem_pares = 0
for numero in numeros:
    if numero % 2 == 0:
        soma_pares += numero
        contagem_pares += 1
        
if contagem_pares > 0:
    media_pares = soma_pares / contagem_pares
    print("A média dos números pares na lista é:", media_pares)
else:
    print("Não há números pares na lista.")
    
