from enum import IntEnum


class АgeGroups(IntEnum):
    '''Перечисление содержит информацию
    о возрастных группах'''
    CHILD = 16
    YOUNG = 20
    MATURE_AGE_1 = 34
    MATURE_AGE_2 = 59
    ELDERLY = 74
    SENILE = 89
    SENTENARIANS = 150


maxim_age = АgeGroups.MATURE_AGE_2
print(maxim_age.value > АgeGroups.CHILD.value)
print(15 < АgeGroups.CHILD.value)
