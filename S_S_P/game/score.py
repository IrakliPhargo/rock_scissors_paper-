from typing import List

from S_S_P.game.settings import MAX_RECORDS_NUMBER


class ScoreHandler:
    def __init__(self, game_record: 'GameRecord', file_name: str) -> None:
        self.game_record: 'GameRecord' = game_record
        self.file_name: str = file_name
        self.read()

    def read(self) -> None:
        with open(self.file_name, 'r') as file:
            lines: List[str] = file.readlines()
            for line in lines:
                parts: List[str] = line.strip().split()
                record: 'PlayerRecord' = PlayerRecord(name=parts[0], mode=parts[1], score=int(parts[2]))
                self.game_record.records.append(record)

    def save(self, player: 'Player') -> None:
        record: 'PlayerRecord' = PlayerRecord(name=player.name, mode=self.game_record.mode, score=player.score)
        self.game_record.add_record(record)
        self.game_record.prepare_records()
        with open(self.file_name, 'w') as file:
            for rec in self.game_record.records:
                file.write(f"{rec.name} {rec.mode} {rec.score}\n")

    def display(self) -> None:
        self.game_record.display()


class GameRecord:
    def __init__(self) -> None:
        self.mode = None
        self.records: List['PlayerRecord'] = []

    def add_record(self, record: 'PlayerRecord') -> None:
        for rec in self.records:
            if rec == record:
                rec.score = max(rec.score, record.score)
                return
        self.records.append(record)

    def prepare_records(self) -> None:
        self.records = sorted(self.records, key=lambda x: x.score, reverse=True)[:MAX_RECORDS_NUMBER]

    def display(self) -> None:
        for rec in self.records:
            print(rec)


class PlayerRecord:
    def __init__(self, name: str, mode: str, score: int) -> None:
        self.name: str = name
        self.mode: str = mode
        self.score: int = score

    def __eq__(self, other: 'PlayerRecord') -> bool:
        return self.name == other.name and self.mode == other.mode

    def __gt__(self, other: 'PlayerRecord') -> bool:
        return self.score > other.score

    def __str__(self) -> str:
        return f"{self.name} {self.mode} {self.score}"
