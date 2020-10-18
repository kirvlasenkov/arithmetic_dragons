# coding: utf-8
# license: GPLv3
from gameunit import *
from typing import Optional

#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.

"""

class Hero(Attacker):
    '''
    Class of the positive character.
    Controlled by the user.
    '''
    def __init__(self, name: Optional[str] = None) -> None:
        self.__name = name

    def attack(self, target:int =0) -> None:
        super().attack(target=0)