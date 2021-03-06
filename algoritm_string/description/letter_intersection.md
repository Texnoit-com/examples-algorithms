# Найти пересекающие символы в двух строках

Даны две строки, выведите все общие символы в алфавитном порядке. Если общих букв нет, выведите '-1'. Все буквы строчные.

Пример:

**Вход :**
string1 : гики
string2: форгики
**Вывод:** гиик
Объяснение: Буквы, которые являются общими между двух строк: **и** (2 раза), **г** (1 раз) и
**к** (1 раз).

Вход :
string1 : hhhello
строка2 : gfghhmh
Выход: hhh

### Решение

1. Преобразуйте обе строки в тип данных словарь с помощью метода Counter(str) , который содержит символы строки в качестве ключа и их частоты в качестве значения.
2. Теперь найдите общие элементы между двумя словарями, используя свойство пересечения ( a&b ) .
3. Результатом также будет встречный словарь, имеющий общие элементы в качестве ключей и их общие частоты в качестве значений.
4. Используйте метод elements() словаря, чтобы расширить список ключей по частоте их появления.
5. Отсортируйте список и соедините каждый символ выходного списка без пробела используя метод join(), чтобы напечатать результирующую строку.