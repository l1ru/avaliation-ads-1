operation = 0
while operation != 7:
    print("Menu")
    print("1. Digite 5 numeros")
    print("2. Media aritmetica")
    print("3. Media ponderado")
    print("4. Desvio padrão")
    print("5. Maior numero")
    print("6. Menor numero")
    print("7. Sair")
    operation = int(input("Digite a opção: "))
    if operation == 1:
        list = []
        for i in range(5):
            list.append(int(input(f"Digite o {i+1} numero: ")))
    elif operation == 2:
        print(f"A media aritmetica é {sum(list)/len(list)}")
    elif operation == 3:
        print(f"A media ponderada é {sum(list)/len(list)*len(list)}")
    elif operation == 4:
        print(f"O desvio padrão é {(sum(list)/len(list))**2}")
    elif operation == 5:
        print(f"O maior numero é {max(list)}")
    elif operation == 6:
        print(f"O menor numero é {min(list)}")
    elif operation == 7:
        print("Saindo...")
        break