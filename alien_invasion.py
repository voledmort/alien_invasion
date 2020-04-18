import pygame

from alien import Alien
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
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

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建游戏统计信息实例
    stats = GameStats(ai_settings)
    # 创建记分牌
    sb = Scoreboard(ai_settings, screen, stats)
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
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        # 确保还有命继续游戏
        if stats.game_active:
            ship.update()
            # 更新子弹位置并删除已消失的子弹
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # 每次循环都会重新绘制屏幕，所以每次都把背景色设置上
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()