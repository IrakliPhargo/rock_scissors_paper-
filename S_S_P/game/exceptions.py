class GameOver(Exception):
    def __init__(self, message="Game Over", *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.message = message


class EnemyDown(Exception):
    def __init__(self, message="Enemy Down", *args, **kwargs):
        super().__init__(message, *args, **kwargs)
        self.message = message
