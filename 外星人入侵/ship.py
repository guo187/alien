import pygame
from  pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        #初始化飞船，并设置其初始位置
        super(Ship,self).__init__()
        #使飞船对象拥有screen属性
        self.screen=screen
        #将游戏设置参数作为ship对象属性
        self.ai_settings=ai_settings
        #加载飞船图像
        self.image=pygame.image.load('Pic/2.bmp')
        #飞船的外接矩形rectangle
        self.rect=self.image.get_rect()
        #屏幕screen的外接矩形
        self.screen_rect=screen.get_rect()
        #飞船初始位置：横向居中，纵向底部对齐
        #飞船矩形中心点横坐标x=窗口中心横坐标X
        self.rect.centerx=self.screen_rect.centerx
        #飞船矩形底部纵坐标y=
        self.rect.bottom=self.screen_rect.bottom
        self.center=float(self.rect.centerx)
        #向右移动
        self.moving_right=False
        self.moving_left=False
    #在指定位置绘制飞船
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        #当飞船的右边界小于窗口的右边界
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center +=self.ai_settings.ship_speed_factor
        #当飞船左边界小于窗口的左边界（零）
        elif self.moving_left and self.rect.left>0:
            self.center -=self.ai_settings.ship_speed_factor
        self.rect.centerx=self.center
    def center_ship(self):
        self.center=self.screen_rect.centerx

