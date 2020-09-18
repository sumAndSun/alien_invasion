import pygame
from pygame.sprite import Sprite

class Alient(Sprite):

    def __init__(self, ai_setting, screen):
        self.ai_setting = ai_setting
        self.screen = screen
        super().__init__()

        # 加载外星人图像
        self.image = pygame.image.load('images/aship.png')
        self.rect = self.image.get_rect()
        # 每个人外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人准确位置
        self.x = float(self.rect.x)



    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def check_deges(self):
        screen_rect = self.screen.get_rect()
        # 当位于边缘返回True
        if self.rect.right > screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """负数向左，正数向右移动外星人"""
        self.rect.x += self.ai_setting.alien_speed_factor * self.ai_setting.fleet_direction

