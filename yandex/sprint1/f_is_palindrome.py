'''Помогите Васе понять, будет ли фраза палиндромом
Учитываются только буквы и цифры, заглавные и строчные
буквы считаются одинаковыми.'''


import re


def is_palindrome(line: str) -> bool:
    line = line.lower()
    opt = re.sub(r'[^\w\s]', '', line)
    opt = opt.replace(' ', '')
    if opt == opt[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_palindrome(input().strip()))
