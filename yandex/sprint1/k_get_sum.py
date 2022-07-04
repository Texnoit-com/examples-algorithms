from typing import List, Tuple


def get_sum(number_list: List[int], k: int) -> List[int]:
    number_list = int(''.join(map(str, number_list)))
    number_list += k
    return [int(i) for i in str(number_list)]


def read_input() -> Tuple[List[int], int]:
    input()
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k


if __name__ == '__main__':
    number_list, k = read_input()
    print(" ".join(map(str, get_sum(number_list, k))))
