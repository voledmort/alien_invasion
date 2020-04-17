import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

    # 初始化游戏
    pygame.init()
    # 初始化游戏设置
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建飞船
    ship = Ship( ai_settings, screen)

    # 游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ship)
        ship.update()
        # 每次循环都会重新绘制屏幕，所以每次都把背景色设置上
        gf.update_screen(ai_settings, screen, ship)

run_game()