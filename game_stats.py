class GameStats():
    def __init__(self, ai_sett):
        self.ai_sett = ai_sett
        self.reset_stats()
        self.game_active = False
        self.record = 0
    def reset_stats(self):
        self.rocket_crush = self.ai_sett.rocket_limit
        self.score = 0
        self.level = 1