import pygame

from alien import Alien
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():

    # 初始化游戏
    pygame.init()
    # 初始化游戏设置
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建飞船
    ship = Ship(ai_settings, screen)
    # 创建子弹
    bullets = Group()
    # 创建外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        # 更新子弹位置并删除已消失的子弹
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        # 每次循环都会重新绘制屏幕，所以每次都把背景色设置上
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()