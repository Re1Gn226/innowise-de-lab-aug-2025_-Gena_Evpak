height = int(input("Введите высоту прямоугольника: "))
width = int(input("Введите ширину прямоугольника: "))

for h in range(height):
    for w in range(width):
        print("*", end=" ")
    print()