from game.exceptions import EnemyDown, GameOver
from game.game import Game
from game.models import Player
from game.score import ScoreHandler, GameRecord
from game.settings import MODES, SCORE_FILE
from typing import Optional

def main() -> None:
    while True:
        print("1. Запустить игру\n2. Посмотреть очки\n3. Выйти из игры")
        choice: str = input("Выберите действие (1, 2, 3): ")

        if choice == '1':
            play_game()
        elif choice == '2':
            show_scores()
        elif choice == '3':
            exit_game()
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")

def play_game() -> None:
    player: Player = create_player()
    game: Game = Game(player=player, mode=player.mode)

    try:
        game.play()
    except GameOver as e:
        print(e)
        game.save_score()

    except EnemyDown as e:
        print(e)
        game.create_enemy()

def create_player() -> Player:
    name: str = input("Введите ваше имя: ")

    while True:
        print("Выберите уровень сложности:")
        print("1. Нормальный")
        print("2. Сложный")
        mode_choice: str = input("Выберите уровень сложности (1, 2): ")

        if mode_choice in MODES:
            mode: str = MODES[mode_choice]
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1 или 2.")

    return Player(name=name, mode=mode)

def show_scores() -> None:
    handler: ScoreHandler = ScoreHandler(game_record=GameRecord(), file_name=SCORE_FILE)
    handler.display()

def exit_game() -> None:
    print("Выход из игры.")
    exit()

if __name__ == "__main__":
    main()
