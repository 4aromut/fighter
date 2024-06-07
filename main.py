from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Удар мечом"

class Bow(Weapon):
    def attack(self):
        return "Выстрел из лука"

class Fighter:
    def __init__(self, weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon):
        self.weapon = weapon

    def fight(self):
        print("Боец выбирает", self.weapon.__class__.__name__)
        print("Боец", self.weapon.attack())
        print("Монстр побежден!")

# Пример использования
fighter = Fighter(Sword())
fighter.fight()

fighter.changeWeapon(Bow())
fighter.fight()