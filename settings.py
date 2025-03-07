class Settings:
    """ 储存游戏《Alien Invasion》中所有设置的类 """

    def __init__(self):
        """ 初始化游戏静态设置 """
        # 屏幕设置
        self.screen_width = 1100
        self.screen_height = 600
        self.background_color = (25,25,25)

        # 飞船设置
        self.ship_speed = 1.5
        self.ships_limit = 3

        # 子弹设置
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,69,0)
        self.bullets_allowed = 8

        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 20
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

        # 按钮设置
        self.button_width = 200
        self.button_height = 50 

        # 加快游戏节奏的速度
        self.speedup_scale = 1.2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ 初始化随游戏进行而变化的设置 """
        self.ship_speed = 1.5
        self.bullet_speed = 2
        self.alien_speed = 1.0
        # fleet_direction为1表示向右，为-1表示向左
        self.fleet_direction = 1
        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """ 提高速度和分值设置 """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.speedup_scale)
        print(self.alien_points)