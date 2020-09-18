import sys
import pygame
import time
from bullet import Bullet
from alient import Alient

# 开火
def fire_bullet(ai_setting, screen, ship, bulltes):
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bulltes) < ai_setting.bullet_allowed:
        new_bullte = Bullet(ai_setting, screen, ship)
        bulltes.add(new_bullte)

# 按下键盘监听事件
def check_keydown_events(event, ai_setting, screen, ship, bulltes):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并将其加入到编组bullets中
        fire_bullet(ai_setting, screen, ship, bulltes)
    elif event.key == pygame.K_q:
        sys.exit()

# 按完键盘后的事件
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

"""当玩家单机开始时，开始游戏"""
def check_play_button(ai_setting, sb, screen, ship, aliens, buttles ,stats, play_button, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    """防止paly区域重复点击时，重置游戏"""
    if button_clicked and not stats.game_active:
        """隐藏光标"""
        pygame.mouse.set_visible(False)
        """还原初始化设置"""
        ai_setting.initialize_dynamic_setting()
        """充值统计信息"""
        stats.rest_stats()
        stats.game_active = True

        """充值记分分牌图像"""
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ship()

        aliens.empty()
        buttles.empty()
        create_fleet(ai_setting, screen, ship, aliens)
        ship.ship_center()

def check_events(ai_setting, sb, stats, screen, ship, aliens, bulltes, play_button):
    """响应按键盘和鼠标时间"""
    for event in pygame.event.get():
        # 点击窗口关闭时，退出
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_setting, screen, ship, bulltes)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_setting, sb, screen, ship, aliens, bulltes, stats, play_button, mouse_x, mouse_y)

def check_bullet_alient_collections(ai_setting, stats, sb, screen, ship, bulltes, aliens):
    """检测子弹是否与外星人发生了碰撞，发生碰撞就删除该外星人"""
    " True是删除发生碰撞得子弹和外星人 ，当第三个参数为False，表示子弹击中外星人时，子弹继续存在一直达到屏幕顶端"
    collections = pygame.sprite.groupcollide(bulltes, aliens, True, True)
    if collections:
        for aliens in collections.values():
            stats.score += ai_setting.alien_points * len(aliens)
            sb.prep_score()
        check_hight_score(stats, sb)
    if len(aliens) == 0:
        bulltes.empty()
        ai_setting.increase_speed()
        stats.level += 1
        """调用prep_level 确保正确显示等级"""
        sb.prep_level()
        create_fleet(ai_setting, screen, ship, aliens)

def update_bullets(ai_setting, stats, sb, screen, ship, bulltes, aliens):
    bulltes.update()
    # 删除已经消失的子弹
    for bullte in bulltes.copy():
        if bullte.rect.bottom <= 0:
            bulltes.remove(bullte)
    check_bullet_alient_collections(ai_setting, stats, sb, screen, ship, bulltes, aliens)

#"""单个外星人绘制"""
# def update_screen(ai_setting, screen, ship, bulltes, alien):
#     # 每次循环时重绘屏幕
#     screen.fill(ai_setting.bg_color)
#     # 在飞船和外星人后面重绘所有子弹
#     for bullte in bulltes.sprites():
#         bullte.draw_bullet()
#     ship.blitme()
#     alien.blitme()
#     # 让最近绘制得屏幕可见
#     pygame.display.flip()

def update_screen(ai_setting,  screen, stats, sb,ship, bulltes, aliens, play_botton):
    # 每次循环时重绘屏幕
    screen.fill(ai_setting.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullte in bulltes.sprites():
        bullte.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    if not stats.game_active:
        play_botton.draw_button()
    """显示得分"""
    sb.show_socre()
    # 让最近绘制得屏幕可见
    pygame.display.flip()

def get_number_aliens_x(ai_setting, alien_width):
    avaliable_space_x = ai_setting.screen_width - 2 * alien_width
    number_alien_x = int(avaliable_space_x/(2 * alien_width))
    return number_alien_x

def create_alien(ai_setting, screen, alien_number, aliens, row_number):
    alien = Alient(ai_setting, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.rect.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien_height + 2 * alien_height * row_number
    aliens.add(alien)
    # alien=Alient(ai_setting,screen)
    # alien_width=alien.rect.width
    # alien_height=alien.rect.height
    # alien.rect.x=alien_width+2*alien_width*alien_number
    # alien.rect.y=alien_height+2*alien_height*row_number
    # aliens.add(alien)

def get_number_rows(ai_setting, ship_height, alien_height):
    avaliable_space_y = ai_setting.screen_hight - 3 * alien_height - ship_height
    numbrs_rows = int(avaliable_space_y/(2 * alien_height))
    return numbrs_rows


def create_fleet(ai_setting, screen, ship, aliens):
     """创建外星人群"""
     """创建外星人，并计算一行可容纳多少外星人个数"""
     """外星人间距为外星人高度"""
     alien = Alient(ai_setting, screen)
     number_aliens_x = get_number_aliens_x(ai_setting, alien.rect.width)
     number_rows = get_number_rows(ai_setting, ship.rect.height, alien.rect.height)
     for row_number in range(number_rows):
         for alien_number in range(number_aliens_x):
             create_alien(ai_setting, screen, alien_number, aliens, row_number)


def check_fleet_direction(ai_setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1

def check_fleet_edges(ai_setting, aliens):
    """外星人到达边缘时"""
    for alien in aliens.sprites():
        if alien.check_deges():
            check_fleet_direction(ai_setting, aliens)
            break

def ship_hit(ai_setting, sb, screen, stats, ship, buttles, aliens):
    if stats.ships_left > 0:
        # ship_left减去1
        stats.ships_left -= 1
        aliens.empty()
        buttles.empty()
        create_fleet(ai_setting, screen, ship, aliens)
        time.sleep(0.5)
        """更新飞船数"""
        sb.prep_ship()
    else:
        stats.game_active = False
        """显示光标"""
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_setting, screen, stats, aliens, buttles, ship):
    """检查外星人是否到达底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_setting, screen, stats, ship, buttles, aliens)

def update_alien(ai_setting, sb, screen, stats, aliens, buttles, ship):
    """更新外星人群众所有外星人得位置"""
    check_fleet_edges(ai_setting, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_setting, sb, screen, stats, ship, buttles, aliens)
    check_aliens_bottom(ai_setting, screen, stats, aliens, buttles, ship)


def check_hight_score(stats, sb):
    if stats.score > stats.higth_score:
        stats.higth_score = stats.score
        sb.prep_high_score()
