'''repeat - итератор, который возвращает всегда один объект'''


from itertools import repeat

repearter = repeat('PY')
next(repearter)  # PY
next(repearter)  # PY
next(repearter)  # PY

list(repeat('PY', 2))
