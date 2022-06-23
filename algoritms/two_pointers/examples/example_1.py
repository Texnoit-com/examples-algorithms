'''Нужно найти максимальное число одинаковых подряд идущих символов в строке'''


def max_consecutive_elements(array_str: str) -> int:
    result: int = 0
    first_pointer: int = 0

    while first_pointer < len(array_str):
        second_pointer: int = first_pointer
        while second_pointer < len(array_str) \
            and array_str[second_pointer] == array_str[first_pointer]:
            second_pointer += 1
        result = max(result, second_pointer - first_pointer)
        first_pointer = second_pointer
    return result


if __name__ == "__main__":
    array_str: str = 'aasserwsafffdsdff dssdffeww'
    print(max_consecutive_elements(array_str))
