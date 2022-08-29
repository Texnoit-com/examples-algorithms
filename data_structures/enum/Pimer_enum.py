from enum import Enum


class АgeGroups(Enum):
    '''Перечисление содержит информацию
    о возрастных группах'''
    CHILD = (0, 16)
    YOUNG = (17, 20)
    MATURE_AGE_1 = (21, 34)
    MATURE_AGE_2 = (35, 59)
    ELDERLY = (60, 74)
    SENILE = (75,   89)
    SENTENARIANS = (90, 150)


maxim_age = АgeGroups.MATURE_AGE_2
print(maxim_age.value)
