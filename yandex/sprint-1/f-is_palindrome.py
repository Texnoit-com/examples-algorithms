'''Помогите Васе понять, будет ли фраза палиндромом
Учитываются только буквы и цифры, заглавные и строчные 
буквы считаются одинаковыми.'''


import re


def is_palindrome(line: str) -> bool:
    line = line.lower()
    opt = re.sub(r'[^\w\s]','', line)
    opt = opt.replace(' ', '')
    if opt == opt[::-1]:
        return True
    else:
        return False

#print(is_palindrome(input().strip()))
assert (is_palindrome('A man, a plan, a canal: Panama')) == True
assert (is_palindrome('e.')) == True
