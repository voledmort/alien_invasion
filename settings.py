class Settings():
    """存储所有设置"""

    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # 外星人
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # 1表示向右移动，-1表示左移
        self.fleet_direction = 1