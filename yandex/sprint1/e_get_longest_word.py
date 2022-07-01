'''Берётся случайное предложение из текста и в нём ищется самое длинное слово'''

def get_longest_word(line: str) -> str:
    arr: list = line.strip().split()
    return max(arr, key=len)


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

#print_result(get_longest_word(read_input()))
