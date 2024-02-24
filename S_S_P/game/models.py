from random import choice

from S_S_P.game.exceptions import GameOver, EnemyDown
from S_S_P.game.settings import PLAYER_LIVES, ALLOWED_ATTACKS


class Player:
    def __init__(self, name: str, mode: str) -> None:
        self.name: str = name
        self.mode: str = mode
        self.lives: int = PLAYER_LIVES
        self.score: int = 0

    def select_attack(self) -> int:
        while True:
            try:
                print("1. Камень\n2. Ножницы\n3. Бумага")
                attack: int = int(input(f"{self.name}, выберите атаку (1, 2, 3):"))
                if attack not in ALLOWED_ATTACKS:
                    raise ValueError("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")
                return attack
            except ValueError as e:
                print(e)

    def decrease_lives(self) -> None:
        self.lives -= 1
        print(f"{self.name} проиграл(а) бой!")
        if self.lives <= 0:
            raise GameOver(f"{self.name} проиграл(а) игру!")

    def add_score(self, points: int) -> None:
        self.score += points
        print(f"{self.name} получил(а) {points} очков.")

class Enemy:
    def __init__(self, level: int, difficulty: int) -> None:
        self.lives: int = level * difficulty
        self.level: int = level

    def select_attack(self) -> int:
        return choice(list(ALLOWED_ATTACKS.keys()))

    def decrease_lives(self) -> None:
        self.lives -= 1
        print("Соперник проиграл(а) бой!")
        if self.lives <= 0:
            raise EnemyDown("Соперник проиграл(а) игру!")
