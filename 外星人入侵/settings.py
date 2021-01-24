#创建类Setting
#类名首字母大写
class Settings():
    #init左右各带两个下划线
    #——init--，构造函数
    #当settings类初始化为对象
    #self为对象本身
    def __init__(self):
        #设置对象属性
        self.screen_width=1000
        self.screen_height =600
        self.bg_color =(230,230,230)
        # self.bg_image=("3.bmp")
        #飞船速度系数
        self.ship_speed_factor=1.5
        self.ship_limit=3
        #子弹的设置
        self.bullet_speed_factor=3
        self.bullet_width=4
        self.bullet_height=15
        self.bullet_color=123,104,238
        self.bullets_allowed=3
        #外星人设置
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        self.speedup_scale=1.1
        self.score_scale=1.5
        self.initialize_dynamic_settings()
        self.fleet_direction=1
    def initialize_dynamic_settings(self):
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1
        self.fleet_direction=1
        self.alien_points=50
    def increase_speed(self):
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scale)
        print(self.alien_points)
