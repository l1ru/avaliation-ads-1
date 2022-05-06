import os

os.system("cls")

list = [
    [135, 134, 13, 123, 64],
    [98, 42, 654, 25, 73],
    [18, 35, 65, 76, 13],
    [9, 542, 34, 13, 675],
    [4, 35, 54, 76, 1341]
]

p = 0
s = 5

principal = 0
secondary = 0

maxPrincipal = {
    "value": 0,
    "index": 0,
}

minPrincipal = {
    "value": 0,
    "index": 0,
}

for i in range(len(list)):
    for j in range(len(list[i])):
        if p == j:
            principal += list[i][j]
            if maxPrincipal["value"] < list[i][j]:
                maxPrincipal["value"] = list[i][j]
                maxPrincipal["index"] = j + 1
            if minPrincipal["value"] > list[i][j] or minPrincipal["value"] == 0:
                minPrincipal["value"] = list[i][j]
                minPrincipal["index"] = j + 1
        if s == j:
            secondary += list[i][j]
            if i == 3:
                secondary += list[len(list)-1][0]
        if j == 4:
            p += 1
        if j == 0:
            s -= 1

print(f"Diferença entre as diagonais: {principal - secondary}")
print(f"O maior valor presente na diagonal principal: {maxPrincipal['value']} na posição {maxPrincipal['index']}")
print(f"O menor valor presente na diagonal principal: {minPrincipal['value']} na posição {minPrincipal['index']}")
