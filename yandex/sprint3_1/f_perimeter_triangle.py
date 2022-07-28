'''Дан массив целых чисел, в котором каждый элемент обозначает длину
стороны треугольника. Нужно определить максимально возможный периметр
треугольника, составленного из сторон с длинами из заданного массива.
Помогите Рите скорее закончить игру и пойти спать.
Напомним, что из трёх отрезков с длинами a ≤ b ≤ c можно составить треугольник,
если выполнено неравенство треугольника: c < a + b'''


def perimeter_triangle(sides):
    sides = list(map(int, sides.split(' ')))
    sides.sort()
    while sides:
        base = sides.pop()
        lenght = len(sides)
        for i in range(lenght):
            for j in range(lenght-1):
                if base < (sides[lenght-1-i] + sides[lenght-2-j]):
                    return base + sides[lenght-1-i] + sides[lenght-2-j]


if __name__ == '__main__':
    _ = input()
    print(perimeter_triangle(input()))
