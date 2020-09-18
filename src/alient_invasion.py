import pygame
from pygame.sprite import Group
from setting import Setting

# 外星人入侵
from ship import Ship
import game_functions as gf
# from alient import Alient
from game_stats import GameStats
from button import Button
from scorebord import Scorebord



def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_hight))
    pygame.display.set_caption("Alien Invasion")
    play_botton = Button(ai_setting, screen, "Play")
    # 创建飞船
    ship = Ship(ai_setting, screen)
    # 创建子弹
    bulltes = Group()
    # 创建外星人
    # alien = Alient(ai_setting, screen)
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_setting, screen, ship, aliens)
    # 存储游戏统计信息得实例
    stats = GameStats(ai_setting)
    # 创建计分牌
    sb = Scorebord(ai_setting, screen, stats)

    # 开始游戏得主要循环
    while True:
        # 监视鼠标和键盘事件
        gf.check_events(ai_setting, sb, stats, screen, ship, aliens, bulltes, play_botton)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_setting, stats, sb, screen, ship, bulltes, aliens)
            gf.update_alien(ai_setting, sb, screen, stats, aliens, bulltes, ship)
           # gf.update_screen(ai_setting, screen, ship, bulltes, alien)
        gf.update_screen(ai_setting, screen, stats, sb, ship, bulltes, aliens,play_botton)

run_game()