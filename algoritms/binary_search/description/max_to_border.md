# Поиск наибольшего числа в упрорядоченном массиве с условием

Дан упорядоченный массив и число X, нужно найти максимальный элемент массива, не превосходящего X.
Если такого элемента не существует, вернуть -1.

Пример:

Ввод: 
```python
array = [5, 7, 9, 12, 15, 18, 19, 20, 22]
x = 17
```
**Результат: 15.** 
 
### Решение

1. Так как массив отсортирован, то используется метод бинарного поиска
2. Массив делиться на две части и средний элемент сравнивается с искомым числом
3. Если средний элемент больше числа X, отбрасывается правая часть массива, а среднее число запоминается
4. Если средний элемент меньше числа X, отбрасывается левая часть, а среднее число запоминается
5. Шаги 2-4 повторяются, пока не будет найден элемент или установленно его отсутствие