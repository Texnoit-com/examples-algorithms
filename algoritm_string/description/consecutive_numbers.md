# Максимальная длина последовательных единиц в двоичной строке

Нам дана двоичная строка, содержащая 1 и 0. Найдите в нем максимальную длину последовательных единиц.

Пример:
```python
Input : str = '11000111101010111'
Output : 4
```
### Решение
1. Разделите все подстроки последовательных единиц, разделенных нулями, используя метод строки split().
2. Выведите максимальную длину разделенных подстрок из 1 применяя к кахжой строке функцию len(), используя функцию map().
3. Найдите максимальную длину используя функцию max()