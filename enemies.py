# coding: utf-8
# license: GPLv3

from gameunit import Attacker
from random import choice, randint
from typing import Union, List
from scipy.misc import derivative
import numpy as np


class Enemy(Attacker):
    """
    Abstract class for the declaring enemy group.
    """
    pass


def generate_random_enemy():
    """
    Picks a random enemy from enemy_types list
    and returns one.
    """
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number) -> List:
    '''
    returns a list with
    a random sequence of enemies

    :param  enemy_number: number of enemies
    '''
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    '''
    Superclass for dragons.
    '''
    def set_answer(self, answer) -> None:
        '''
        Set an actual answer received from user.
        :param answer: user answer
        '''
        self.__answer = answer

    def check_answer(self, answer):
        """
        Checks is it user answer correct or not.
        "param answer: user answer
        """
        return answer == self.__answer

    def question(self):
        '''
        Problem, which user should solve.
        '''
        raise NotImplementedError


class GreenDragon(Dragon):
    '''
    Dragon, which produce mathematical problems,
    connected with addition.
    '''
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'green'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + ' + ' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragon(Dragon):
    '''
    Dragon, which produce mathematical problems,
    connected with subtraction.
    '''
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'red'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + ' - ' + str(y)
        self.set_answer(x - y)
        return self.__quest


class BlackDragon(Dragon):
    '''
    Dragon, which produce mathematical problems,
    connected with multiplication.
    '''
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'black'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest


class DifferentialDragon(Dragon):
    '''
    Dragon, which produce mathematical problems,
    connected with differential calculus.
    '''
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'differential'

    @staticmethod
    def polynom(x: Union[int, float], degree: int = 2,):
        poly_coefs = [randint(0, 6) for _ in range(degree)]
        ans = 0
        for _ in range(len(poly_coefs)):
            ans +=

    def question(self):


class IntegralDragon(Dragon):
    '''
    Dragon, which produce mathematical problems,
    connected with integral calculus.
    '''
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'integral'

    pass


class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


# FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.


enemy_types = [GreenDragon, RedDragon, BlackDragon,
               DifferentialDragon, IntegralDragon, Troll]
