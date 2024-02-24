from typing import Optional

from S_S_P.game.exceptions import GameOver, EnemyDown
from S_S_P.game.models import Player, Enemy
from S_S_P.game.score import ScoreHandler, GameRecord
from S_S_P.game.settings import MODES, ALLOWED_ATTACKS, ATTACK_PAIRS_OUTCOME, WIN, POINTS_FOR_FIGHT, LOSE, SCORE_FILE


class Game:
    def __init__(self, player: Player, mode: str) -> None:
        self.player: Player = player
        self.enemy: Optional[Enemy] = None
        self.mode: str = mode

    def create_enemy(self, enemy_level=1, enemy_difficulty=MODES) -> None:
        self.enemy = Enemy(level=enemy_level, difficulty=enemy_difficulty)

    def play(self) -> None:
        while True:
            try:
                print("Начало игры")
                self.create_enemy()
                print("Враг создан.")
                self.fight()
                self.handle_fight_result()
            except GameOver as e:
                print(e)
                self.save_score()
                break
            except EnemyDown as e:
                print(e)
                self.create_enemy()

    def fight(self) -> None:
        player_attack: int = self.player.select_attack()
        enemy_attack: int = self.enemy.select_attack()

        print(f"{self.player.name} выбрал(а) {ALLOWED_ATTACKS[player_attack]}")
        print(f"Соперник выбрал {ALLOWED_ATTACKS[enemy_attack]}")

        result: str = ATTACK_PAIRS_OUTCOME[(ALLOWED_ATTACKS[player_attack], ALLOWED_ATTACKS[enemy_attack])]

        if result == WIN:
            print("Вы победили в этом бою!")
            self.player.add_score(POINTS_FOR_FIGHT)
        elif result == LOSE:
            print("Вы проиграли в этом бою!")
            self.player.decrease_lives()
        else:
            print("Ничья!")

    def handle_fight_result(self) -> None:
        if self.player.lives <= 0:
            raise GameOver("У вас закончились жизни.")
        elif self.enemy.lives <= 0:
            raise EnemyDown("Соперник проиграл(а) бой.")

    def save_score(self) -> None:
        handler: ScoreHandler = ScoreHandler(game_record=GameRecord(), file_name=SCORE_FILE)
        handler.save(self.player)
        handler.display()
