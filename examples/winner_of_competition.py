"""Найти победителя конкурса"""

from collections import Counter


def winner(input: list) -> str:
    votes = Counter(input)
    candidates: dict = {}
    for value in votes.values():
        candidates[value] = []
    for (key, value) in votes.items():
        candidates[value].append(key)
    maxVote = sorted(candidates.keys(), reverse=True)[0]
    if len(candidates[maxVote]) > 1:
        return sorted(candidates[maxVote])[0]
    else:
        return candidates[maxVote][0]


if __name__ == "__main__":
    input = ['Анна', 'Виктория', 'Юлия', 'Елена',
             'Анна', 'Юлия', 'Виктория', 'Елена',
             'Анна', 'Елена', 'Елена', 'Виктория',
             'Анна']
    print(winner(input))
