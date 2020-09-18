class GameStats():
    def __init__(self, ai_setting):
        self.ai_setting = ai_setting
        self.game_active = False
        self.score = 0
        # 记录最高得分
        self.higth_score = 0
        # 游戏等级
        self.level = 1
        self.rest_stats()

    def rest_stats(self):
        self.ships_left = self.ai_setting.ship_limit
        self.score = 0
        self.level = 1



