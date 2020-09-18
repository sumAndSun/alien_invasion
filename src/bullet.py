import  pygame
from pygame.sprite import Sprite

# 子弹
class Bullet(Sprite):
    def __init__(self, ai_setting, screen, ship):
        # 继承
        # 2.7语法
        # super(Bullet, self)._init_()
        # 3.0写法
        super().__init__()
        self.screen = screen

        # 在（0，0）处创建子弹形状和子弹位置
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bulltt_height)
        # 子弹和飞船在同一位置，中央
        self.rect.centerx = ship.rect.centerx
        # 子弹位置在飞船位置上
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        # 向上移动子弹，就更新子弹位置的小数值
        # 更新子弹位置小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)