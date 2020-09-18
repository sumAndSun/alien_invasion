import pygame
from pygame.sprite import Group
from ship import Ship

"""显示得分的信息的类"""
class Scorebord():

    def __init__(self, ai_setting, screen, stats):
        self.ai_setting = ai_setting
        self.screen = screen
        self.stats = stats
        self.screen_rect = screen.get_rect()
        # 黑色字体
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        """将得分转换为渲染的图像"""
        rounded_socre = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_socre)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_setting.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        higth_score = int(round(self.stats.higth_score, -1))
        high_score_stc = "{:,}".format(higth_score)
        self.high_score_image = self.font.render(high_score_stc, True, self.text_color, self.ai_setting.bg_color)
        """将最高得分显示在屏幕顶端中央"""
        self.higth_score_rect = self.high_score_image.get_rect()
        self.higth_score_rect.centerx = self.screen_rect.centerx
        self.higth_score_top = self.score_rect.top

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_setting.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_socre(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.higth_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    """显示余下的飞船数"""
    def prep_ship(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_setting, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)