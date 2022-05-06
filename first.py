grades = []

while len(grades) < 3:
    print(f"Digite a nota {len(grades)+1}: ")
    grade = input()
    if grade:
        grades.append(float(grade))

print("\n")

media_grades = sum(grades)/len(grades)
print(f"A média das notas é {media_grades}")

if media_grades >= 9:
    print("A media do aluno esta dentro do conceita A")
elif media_grades >= 7.5 < 9:
    print("A media do aluno esta dentro do conceita B")
elif media_grades >= 6 < 7.5:
    print("A media do aluno esta dentro do conceita C")
elif media_grades >= 4 < 6:
    print("A media do aluno esta dentro do conceita D")
elif media_grades < 4:
    print("A media do aluno esta dentro do conceita E")