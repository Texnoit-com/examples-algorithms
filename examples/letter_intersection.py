'''Найти пересекающие символы в двух строках'''


from collections import Counter


def common(string1: str, string2: str) -> str:
    dict1: dict = Counter(string1)
    dict2: dict = Counter(string2)
    commonDict: dict = dict1 & dict2
    if len(commonDict) == 0:
        return '-1'
    commonChars: list = list(commonDict.elements())
    commonChars: list = sorted(commonChars)
    return ''.join(commonChars)


if __name__ == "__main__":
    string1: str = 'geeks'
    string2: str = 'forgeeks'
    print(common(string1, string2))
