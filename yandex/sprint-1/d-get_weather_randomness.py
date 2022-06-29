'''Метеорологическая служба вашего города решила исследовать погоду 
новым способом. 
- Под температурой воздуха в конкретный день будем понимать 
максимальную  температуру в этот день.
- Под хаотичностью погоды за n дней служба понимает количество дней, 
в которые температура строго больше, чем в день до (если такой существует) 
и в день после текущего (если такой существует). 

Например, если за 5 дней максимальная температура воздуха составляла [1, 2, 5, 4, 8] 
градусов, то хаотичность за этот период равна 2: в 3-й и 5-й дни выполнялись описанные условия.
Определите по ежедневным показаниям температуры хаотичность погоды за этот период.

Заметим, что если число показаний n=1, то единственный день будет хаотичным.'''


from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    n: int = 0
    l = len(temperatures)
    if l == 1:
        return 1
    if temperatures[0] > temperatures [1]:
        n+=1
    for i in range(l-2):
        if temperatures[i] < temperatures [i+1] and temperatures[i+1] > temperatures[i+2]:
            n +=1
    if temperatures[l-1] > temperatures[l-2]:
        n+=1
    return n

def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures

temperatures = read_input()
print(get_weather_randomness(temperatures))

assert get_weather_randomness([-1,-10,-8,0,2,0,5]) == 3
assert get_weather_randomness([5,5,5,5,5,5,5]) == 0
assert get_weather_randomness([-159, -248, 8, -23, -45, -131, -169, -184, 159, -241]) == 3
assert get_weather_randomness([-159,]) == 1
