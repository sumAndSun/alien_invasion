class Setting():
    """存储《外星人入侵》所有得设置类"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_hight = 800
        # 背景色
        self.bg_color = (230, 230, 230)
        # 飞船速度设置
        self.ship_limit = 3

        # 设置子弹
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bulltt_height = 15
        # 灰色
        self.bullet_color = 60, 60, 60
        # 设置子弹最大数
        self.bullet_allowed = 3
        # 控制外星人移动速度

        # 当外星人撞到边缘，下移速度
        self.fleet_drop_speed = 10


        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 记分
        self.alien_points = 50
        # 外星人点数提高速度
        self.score_scale = 1.5


    def initialize_dynamic_setting(self):
        """初始化游戏设置的变化设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # -1向左;1向右
        self.fleet_direction = 1


    def increase_speed(self):
        """提高速度"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

