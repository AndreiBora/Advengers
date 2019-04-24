import random


class SuperHero:
    def __init__(self, id, name, description, attack, health, isVillain):
        self._id = id
        self._name = name
        self._description = description
        self._attack = attack
        self._health = health
        self._isVillain = isVillain

    def perform_attack(self):
        rand = random.random() * (1.0 - 0.6) + 0.6
        return round(rand * self._attack)

    def damage(self, value):
        # planet can make attack negative
        if value < 0:
            return
        self._health -= value

    def enhance_health(self, value):
        self._health += value

    def enhance_attack(self, value):
        self._attack += value

    def is_alive(self):
        if self._health > 0:
            return True
        return False

    def __str__(self):
        return f'{self._name} (attack: {self._attack} health: {self._health})'
