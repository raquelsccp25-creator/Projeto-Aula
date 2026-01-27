# Parte 1: Usando o laço FOR (Crescente)
for andar in range(1, 21):
    if andar == 13:
        continue
    print(andar)

# Parte 2: Usando o laço WHILE (Crescente)
andar = 1
while andar <= 20:
    if andar != 13:
        print(andar)
    andar += 1

# Parte 3: Ordem Decrescente (Desafio)
for i in range(20, 0, -1):
    if i == 13:
        continue
    print(i)
  
