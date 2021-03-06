import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):

        # 设置飞船初始位置
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 飞船图片
        self.image = pygame.image.load('images/ship.bmp')
        # 像矩形一样处理元素
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将船放在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 将飞船速度设置为可容纳小数
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 更新最终移动的对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """居中飞船"""
        self.center = self.screen_rect.centerx