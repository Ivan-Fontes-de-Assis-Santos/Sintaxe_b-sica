#Exemplo de listas:
Frutas= ["Laranja", "Mamão", "Pera", "Limão"]
print(Frutas)

Vazio= []
print(Vazio)

Letras= list("Engenharia")
print(Letras)

Carro= ["Golf", "GTI", 25000, 1995, "São Paulo", True]
print(Carro)

#Método para pegar os indices de uma lista, ultilizando o método "Acesso Direto":
Frutas= ["Laranja", "Mamão", "Pera", "Limão"]
print(Frutas[0])
print(Frutas[2])

#Listas podem armazenar todos os tipos de objetos em Python, vou dar um exemplo de estruturas bidimensionais(tabelas) e acessar as informações ultilizando o método "Acesso Direto":
Matriz= [
    [1, "z", 4],
    ["v", 6, 0],
    [1, 2, 4]
]
print(Matriz[0])
print(Matriz[1])
print(Matriz[2])
print(Matriz[-2])
print(Matriz[2][-3])

#Podemos usar o método de "Fatiamento" em Python:
Lista= ["J", "o", "g", "o"]
print(Lista[0:])
print(Lista[1:])
print(Lista[2:])
print(Lista[3:])
print(Lista[:0])
print(Lista[:3])

#A forma mais comum para percorrer os dados de uma lista é ultilizando o comando "for" ou "para":
carros= ["Azera", "Tucson", "HB20"]
for carros in carros:
    print(carros)

#O método "Compreensão de listas" serve para criar uma nova lista com vase nos valores de uma lista já existente ou gerar uma nova lista aplicando novas modificação de dados:
Numeros= [1, 40, 41, 42, 43, 44]
Pares= []
for numero in Numeros:
    if numero % 2==0:
        Pares.append(numero)
print(Pares)

Nummeros= [1, 40, 41, 42, 43, 44]
Quadrado= []
for numero in Nummeros:
    Quadrado.append(numero ** 2)
print(Quadrado)