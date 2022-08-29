'''именованный кортеж'''

from collections import namedtuple

User = namedtuple('User', ['first_name', 'last_name', 'age'])
user1 = User('Максим', 'Бекурин', 35)

print(user1)
print(user1.first_name)
