from typing import Dict, Tuple

MODE_NORMAL = 'Normal'
MODE_HARD = 'Hard'
MODES: Dict[str, str] = {'1': MODE_NORMAL, '2': MODE_HARD}

PLAYER_LIVES: int = 2
POINTS_FOR_FIGHT: int = 1
POINTS_FOR_KILLING: int = 5
MAX_RECORDS_NUMBER: int = 5
HARD_MODE_MULTIPLIER: int = 2

SCORE_FILE: str = 'scores.txt'

STONE: str = 'Stone'
SCISSORS: str = 'Scissors'
PAPER: str = 'Paper'

WIN: int = 1
DRAW: int = 0
LOSE: int = -1

ALLOWED_ATTACKS: Dict[int, str] = {
    1: STONE,
    2: SCISSORS,
    3: PAPER
}

ATTACK_PAIRS_OUTCOME: Dict[Tuple[str, str], int] = {
    (STONE, PAPER): LOSE,
    (STONE, STONE): DRAW,
    (STONE, SCISSORS): WIN,
    (SCISSORS, PAPER): WIN,
    (SCISSORS, STONE): LOSE,
    (SCISSORS, SCISSORS): DRAW,
    (PAPER, PAPER): DRAW,
    (PAPER, STONE): WIN,
    (PAPER, SCISSORS): LOSE
}
