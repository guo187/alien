import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf
def run_game():
    #游戏初始化
    pygame.init()
    ai_settings=Settings()
    #子弹编组对象
    bullets=Group()
    aliens=Group()
    pygame.mixer.init()
    pygame.mixer.music.load(r"music/bj.mp3")
    pygame.mixer.music.play()
    #创建一个屏幕对象
    #屏幕尺寸为1200*800
    #背景颜色
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")#字幕
    play_button=Button(ai_settings,screen,"Play")
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)
    # bg_color = (255, 255, 255)
    #创建
    ship=Ship(ai_settings,screen)
    alien=Alien(ai_settings,screen)
    gf.create_fleet(ai_settings, screen, ship,aliens)
    #游戏主循环
    while True:
        #检查事件
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
        #删除已消失的子弹
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        # 更新屏幕
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button )

r=run_game()
print(r)









