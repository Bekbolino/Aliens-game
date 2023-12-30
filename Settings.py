class Settings():
    def __init__(self):
        self.screen_width = 1100
        self.screen_height = 650
        self.bg_color=(22, 26, 30)
        self.alinz_speed_f = 3
        self.bullet_speed_f = 1.5
        self.bullet_width =  3
        self.bullet_height = 15
        self.bullet_color = 0, 225, 0
        self.bullets_allowed = 3
        self.rocket_speed_f = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.rocket_limit = 3
        
        self.speedup_scale = 2
        self.score_scale = 1.5
        self.initialize_dynamic_sett()
    def initialize_dynamic_sett(self):
        self.rocket_speed_f = 1.5
        self.bullet_speed_f = 3
        self.fleet_direction = 1
        self.alinz_point = 50
    def increase_speed(self):
        self.rocket_speed_f *= self.speedup_scale
        self.bullet_speed_f *= self.speedup_scale
        self.alinz_speed_f *= self.speedup_scale