class Settings():
    """Класс для хранения всех настроек игры"""
    def __init__(self):
        self.alien_speed=1
        self.fleet_drop_speed=10
        self.fleet_direction=1
        self.screen_width=1200
        self.screen_height=600
        self.bg_color=(233,233,233)
        self.ship_speed_factor=1.5
        self.bullet_speed=3
        self.bullet_width=2
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=3
        self.ship_limit=3
        self.speed_up_scale=1.1
        self.alien_points=50
        self.score_scale=1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.ship_speed_factor=1.5
        self.score_scale=1.5
        self.bullet_speed=3
        self.alien_speed=1
        self.fleet_direction=1
    def increase_speed(self):
        self.ship_speed_factor*=self.speed_up_scale
        self.bullet_speed*=self.speed_up_scale
        self.alien_speed*=self.speed_up_scale
        self.alien_points*=self.score_scale