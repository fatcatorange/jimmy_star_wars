import pygame
from sys import exit
import os 
from pygame.constants import BUTTON_LEFT
import time
import random
import threading

from pygame.display import update

sourceFileDir = os.path.dirname(os.path.abspath(__file__)) #目前目錄
font_source=os.path.join(sourceFileDir,"fonts") #圖片目錄
font=os.path.join(font_source,"font.ttf")

class MyPLAIN :
    def __init__(self) :
        self.x=300
        self.y=800
        self.plain=pygame.image.load(import_image("plain.png"))
        self.plain_rect=self.plain.get_rect(midbottom=(self.x,self.y))
        self.hp=20

class Enemy1:
    def __init__(self,x):
        self.x=x
        self.y=0
        self.enemy=pygame.image.load(import_image("enemy1.png"))
        self.enemy_rect=self.enemy.get_rect(midbottom=(self.x,self.y))
        self.hp=10
        self.score=10
        self.em_bullet=EnemyBullet(self.x,50)
        self.hurt=1
        self.speed=2

    def move(self):
        if self.enemy_rect.y<=50:
            self.enemy_rect.y+=5
    
    def check_dead(self):
        if self.hp<=0:
            return True

class Enemy2(Enemy1):
    def __init__(self, x):
        super().__init__(x)
        self.enemy=pygame.image.load(import_image("enemy2.png"))
        self.enemy_rect=self.enemy.get_rect(midbottom=(self.x,self.y))
        self.hp=20
        self.score=20
        self.hurt=2
        self.speed=3

class Bullet:
    def __init__(self,plain):
        self.x=plain.plain_rect.midbottom[0]
        self.y=plain.plain_rect.midtop[1]
        self.bullet=pygame.image.load(import_image("bullet.png"))
        self.bullet_rect=self.bullet.get_rect(midbottom=(self.x,self.y))

class EnemyBullet:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.bullet=pygame.image.load(import_image("enemy_bullet.png"))
        self.bullet_rect=self.bullet.get_rect(midbottom=(self.x,self.y))
    
    def check_hit(self,plain,enemy):
        if self.bullet_rect.colliderect(plain.plain_rect):
            self.bullet_rect.y=enemy.enemy_rect.midbottom[1]
            self.bullet_rect.x=enemy.enemy_rect.midbottom[0]
            plain.hp-=enemy.hurt
        if plain.hp<=0:
            explode=pygame.image.load(import_image("explode.png"))
            return True
        return False


def import_image(image_name):
    """sourceFileDir = os.path.dirname(os.path.abspath(__file__)) #目前目錄
    img_source=os.path.join(sourceFileDir,"graphics") #圖片目錄
    return os.path.join(img_source,image_name)"""
    return os.path.join("graphics",image_name)

def start_page():
    ch_font=pygame.font.Font("font.ttf",60)
    title=ch_font.render('JIMMY STAR WARS',False,'white')
    title_rect=title.get_rect(center=(300,100))
    screem.blit(title,title_rect)

    ch_font=pygame.font.Font("font.ttf",40)
    start=ch_font.render('PRESS SPACE TO START',False,'white')
    start_rect=start.get_rect(center=(300,600))
    screem.blit(start,start_rect)

    pygame.display.update()
    clock.tick(60)

    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        return 1
    return 0

class Boss(Enemy1):
    def __init__(self,x):
        super().__init__(x)
        self.x=300
        self.y=0
        self.enemy=pygame.image.load(import_image("boss.png"))
        self.enemy_rect=self.enemy.get_rect(midbottom=(self.x,self.y))
        self.hp=100
        self.score=50
        self.hurt=5
        self.speed=4
        self.em_bullet.bullet=pygame.image.load(import_image("enemy_fireball.png"))
        self.em_bullet.bullet_rect=self.em_bullet.bullet.get_rect(midbottom=(self.x,self.y))
    
    def boss_move(self,plain):
        if self.enemy_rect.center[0]<plain.plain_rect.center[0]:
            self.enemy_rect.x+=1
        else:
            self.enemy_rect.x-=1

class Boss2(Boss):
    def __init__(self, x):
        super().__init__(x)
        self.hp=125
        self.hurt=1.5
        self.speed=11
        self.enemy=pygame.image.load(import_image("boss2.png"))
        self.enemy_rect=self.enemy.get_rect(midbottom=(self.x,self.y))
        self.em_bullet.bullet=pygame.image.load(import_image("light_ball.png"))
        self.em_bullet.bullet_rect=self.em_bullet.bullet.get_rect(midbottom=(self.x,self.y))

class Loading:
    def __init__(self) :
        self.loading=0

def loding_page(loading):
    ch_font=pygame.font.Font("font.ttf",60)
    shiba=pygame.image.load("graphics/strong_shiba.png")
    update='loading'
    
    for i in range(5):
        waiting=ch_font.render(update,False,'white')
        waiting_rect=waiting.get_rect(midleft=(200,300))
        shiba_rect=shiba.get_rect(midtop=((waiting_rect.bottomleft[0]+50),waiting_rect.bottomleft[1]))
        screem.blit(shiba,shiba_rect)
        screem.blit(waiting,waiting_rect)
        update=update+'.'
        pygame.display.update()  
        time.sleep(0.2)


pygame.init()
pygame.display.set_caption("strong jimmy")
icon=pygame.image.load(import_image("shiba.png"))
icon=pygame.transform.scale(icon,(25,19))
pygame.display.set_icon(icon)
screem=pygame.display.set_mode((600,800))
clock=pygame.time.Clock()


loading=Loading()
loading_threat = threading.Thread(target = loding_page(loading))
loading_threat.start()

crash_enemy=0
test_font=pygame.font.Font("font.ttf",20)


background=pygame.image.load(import_image("space.png"))
explode=pygame.image.load(import_image("explode.png"))
hit=pygame.image.load(import_image("hit.png"))
fire=pygame.image.load(import_image("fire.png"))
fire2=pygame.image.load(import_image("fire2.png"))
light=pygame.image.load(import_image("light.png"))
lightball=pygame.image.load(import_image("light_ball.png"))

fireball_sound=pygame.mixer.Sound("audio/fireball.mp3")
explode_sound=pygame.mixer.Sound("audio/explode.mp3")
bgm=pygame.mixer.Sound("audio/bgm.mp3")
gun=pygame.mixer.Sound("audio/gun.mp3")
boss_bgm=pygame.mixer.Sound("audio/boss.mp3")

loading.loading=1
print("in!")

enemys=[]
enemy_position=[]


myPlain=MyPLAIN()
bullets=[]

hp=test_font.render("hp:",False,"white")
hp_rect=hp.get_rect(topleft=(0,0)) 

boss_count=360

now_boss=1

lightcheck=0
round=0
start_game=0
dead=False
boss_battle=0
firecheck=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if start_game==0:
        bgm.stop()
        if(start_page()==1):
            bgm.play(loops=-1)
            start_game=1
    
    screem.blit(background,(0,0))

    if start_game==0:
        continue

    #檢查分數是否到達
    if  crash_enemy>=200 and (crash_enemy%200==0 or crash_enemy%210==0) and boss_battle==0:
        boss_battle=1
    
    #加入魔王，清空小兵 
    if boss_battle==1: #boss_battle: 0:還沒開始 1:發現可以打 2:對打中 3:等待開始
        bgm.stop()
        boss_bgm.play(loops=-1)
        for enemy in enemys:
            screem.blit(explode,(enemy.enemy_rect.topleft))
            enemy_position.pop()
            crash=True
        enemys.clear()
        boss_battle=3
    
    #檢查魔王還在不在
    if boss_battle==2 and len(enemys)==0:
        boss_battle=0
        boss_count=360
        boss_bgm.stop()
        bgm.play(loops=-1)
        now_boss=(now_boss%2)+1

    #魔王還在則移動
    if boss_battle ==2:
        boss.boss_move(myPlain)
    
    if boss_battle == 3:
        boss_count-=1
        if boss_count==0:
            boss_battle=2
            if now_boss==2:
                boss=Boss2(300)
            else:
                boss=Boss(300)
            boss_battle=2
            boss_count-=1
            enemys.append(boss)
            enemy_position.append(300)
            continue
    #分數
    score=test_font.render("score:"+str(crash_enemy),False,"white")
    score_rect=score.get_rect(topleft=(500,0))  

    hp_surface=pygame.Surface((myPlain.hp*20,20)) #血條
    hp_surface.fill('green')

    if round%10==0:
        bullets.append(Bullet(myPlain))
        gun.play()
        if round==3000:
            round=0

    for enemy in enemys:
        enemy.move()
    
    #加入敵人
    if round%150==0 and boss_battle==0:
        for i in range(10):
            check=0
            randx=random.randrange(100,550,100)
            for check_p in enemy_position:
                if check_p==randx:
                    check=1
                    break
            if check==0:
                rand_enemy=random.randrange(0,4)
                if rand_enemy==0:
                    enemys.append(Enemy2(randx))
                else:
                    enemys.append(Enemy1(randx))
                enemy_position.append(randx)
                break
    
    #對方子彈
    for enemy in enemys:
        screem.blit(enemy.enemy,enemy.enemy_rect)
        if enemy.enemy_rect.y>=50:
            if boss_battle==2 and now_boss==1:
                fireball=pygame.image.load(import_image("enemy_fireball.png"))
                fireball2=pygame.image.load(import_image("fireball2.png"))
                if round%10<=5:
                    screem.blit(fireball,((enemy.em_bullet.bullet_rect)))
                else:
                    screem.blit(fireball2,(enemy.em_bullet.bullet_rect))
            else:
                screem.blit(enemy.em_bullet.bullet,(enemy.em_bullet.bullet_rect))
        enemy.em_bullet.bullet_rect.y+=(enemy.speed+crash_enemy/100)
        dead=enemy.em_bullet.check_hit(myPlain,enemy)
        if enemy.em_bullet.bullet_rect.y>=800:
            enemy.em_bullet.bullet_rect.y=enemy.enemy_rect.midbottom[1]
            enemy.em_bullet.bullet_rect.x=enemy.enemy_rect.midbottom[0]
        
    

    #我方子彈檢查
    crash=False
    bullet_count=0
    for now_bullet in bullets:
        screem.blit(now_bullet.bullet,now_bullet.bullet_rect)
        now_bullet.bullet_rect.y-=8
        enemy_count=0
        for enemy in enemys:
            if now_bullet.bullet_rect.colliderect(enemy.enemy_rect) and len(bullets)>0: #檢查有沒有打中
                bullets.pop(bullet_count)
                enemy.hp-=1
                screem.blit(hit,(now_bullet.bullet_rect.topleft[0],now_bullet.bullet_rect.topleft[1]-100))
                if enemy.check_dead() == True: #檢查對方hp
                    explode_sound.play()
                    screem.blit(explode,(enemy.enemy_rect.topleft))
                    enemys.pop(enemy_count)
                    enemy_position.pop(enemy_count)
                    crash=True
                    crash_enemy+=enemy.score
            enemy_count+=1
        if now_bullet.bullet_rect.y<= 0 and len(bullets)>0: #檢查子彈在不再視窗內
            bullets.pop(bullet_count)
        bullet_count+=1
    

    if len(enemys)>0 and crash_enemy>=50:
        pygame.draw.line(screem,'yellow',(myPlain.plain_rect.midleft[0],myPlain.plain_rect.midleft[1]+40),enemys[0].enemy_rect.center,3)
        pygame.draw.line(screem,'red',(myPlain.plain_rect.midleft[0],myPlain.plain_rect.midleft[1]+40),enemys[0].enemy_rect.center,1)
        pygame.draw.line(screem,'yellow',(myPlain.plain_rect.midright[0],myPlain.plain_rect.midleft[1]+40),enemys[0].enemy_rect.center,3)
        pygame.draw.line(screem,'red',(myPlain.plain_rect.midright[0],myPlain.plain_rect.midleft[1]+40),enemys[0].enemy_rect.center,1)
        light_rect=light.get_rect(center=(enemys[0].enemy_rect.center))
        screem.blit(light,light_rect)
        enemys[0].hp-=0.025
        if myPlain.hp<=20:
            myPlain.hp+=0.005
        if enemys[0].check_dead() == True: #檢查對方hp
            screem.blit(explode,(enemys[0].enemy_rect.topleft))
            enemys.pop(0)
            enemy_position.pop(0)
            crash=True
            crash_enemy+=enemy.score

    #火球
    if crash_enemy>=250:
        if firecheck==0:
            fireball=pygame.image.load(import_image("enemy_fireball.png"))
            fireball2=pygame.image.load(import_image("fireball2.png"))
            fireball_rect=fireball.get_rect(midbottom=(myPlain.plain_rect.center))
            fireball_sound.play()
            firecheck=1
        if round%10<=5:
            screem.blit(fireball,fireball_rect)
        else:
            screem.blit(fireball2,fireball_rect)

        if fireball_rect.midbottom==(myPlain.plain_rect.center):
            fireball_sound.play()
        fireball_rect.y-=5
        enemy_count=0
        for enemy in enemys:
            if fireball_rect.colliderect(enemy.enemy_rect):
                fireball_rect=fireball.get_rect(midbottom=(myPlain.plain_rect.center))
                fireball_sound.play()
                enemy.hp-=5
                screem.blit(hit,(fireball_rect.midtop))
                if enemy.check_dead() == True: #檢查對方hp
                    screem.blit(explode,(enemy.enemy_rect.topleft))
                    enemys.pop(enemy_count)
                    enemy_position.pop(enemy_count)
                    crash=True
                    crash_enemy+=enemy.score
            if fireball_rect.y<=0:
                fireball_rect=fireball.get_rect(midbottom=(myPlain.plain_rect.center))
            enemy_count+=1
    #光球
    if  crash_enemy>=450:
        if lightcheck==0:
            lightball_rect=lightball.get_rect(midbottom=(myPlain.plain_rect.midleft[0],myPlain.plain_rect.midleft[1]+40))
            lightball_rect2=lightball.get_rect(midbottom=(myPlain.plain_rect.midright[0],myPlain.plain_rect.midleft[1]+40))
            lightcheck=1

        lightball_rect2.y-=20
        lightball_rect.y-=20

        screem.blit(lightball,lightball_rect)
        screem.blit(lightball,lightball_rect2)
        enemy_count=0
        for enemy in enemys:
            if lightball_rect.colliderect(enemy.enemy_rect):
                lightball_rect=lightball.get_rect(midbottom=(myPlain.plain_rect.midleft[0],myPlain.plain_rect.midleft[1]+40))
                enemy.hp-=2
                screem.blit(hit,(lightball_rect.midtop))
                if enemy.check_dead() == True: 
                    screem.blit(explode,(enemy.enemy_rect.topleft))
                    enemys.pop(enemy_count)
                    enemy_position.pop(enemy_count)
                    crash=True
                    crash_enemy+=enemy.score
            if lightball_rect2.colliderect(enemy.enemy_rect):
                lightball_rect2=lightball.get_rect(midbottom=(myPlain.plain_rect.midright[0],myPlain.plain_rect.midleft[1]+40))
                enemy.hp-=2
                screem.blit(hit,(lightball_rect2.midtop))
                if enemy.check_dead() == True: 
                    screem.blit(explode,(enemy.enemy_rect.topleft))
                    enemys.pop(enemy_count)
                    enemy_position.pop(enemy_count)
                    crash=True
                    crash_enemy+=enemy.score
            enemy_count+=1
        if lightball_rect2.y<=0:
            lightball_rect2=light.get_rect(midbottom=(myPlain.plain_rect.midright[0],myPlain.plain_rect.midleft[1]+40))
        if lightball_rect.y<=0:
            lightball_rect=light.get_rect(midbottom=(myPlain.plain_rect.midleft[0],myPlain.plain_rect.midleft[1]+40))
            

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and myPlain.plain_rect.bottomleft[0]>=0:
        myPlain.plain_rect.x-=5
    if keys[pygame.K_RIGHT] and myPlain.plain_rect.bottomright[0]<=600:
        myPlain.plain_rect.x+=5
    if keys[pygame.K_UP] and myPlain.plain_rect.topright[1]>=0:
        myPlain.plain_rect.y-=5
    if keys[pygame.K_DOWN] and myPlain.plain_rect.bottomright[1]<=800:
        myPlain.plain_rect.y+=5

    fire_rect=fire.get_rect(midtop=(myPlain.plain_rect.midbottom))
    screem.blit(myPlain.plain,(myPlain.plain_rect))
    screem.blit(score,score_rect)
    screem.blit(hp,hp_rect)
    screem.blit(hp_surface,(50,0))
    if round%10<=5:
        screem.blit(fire,fire_rect)
    else:
        screem.blit(fire2,fire_rect)

    round+=1
    if dead==True:
        screem.blit(explode,myPlain.plain_rect.topleft)
    pygame.display.update()
    if crash==True:
        time.sleep(0.1)
    if dead==True:
        time.sleep(0.5)
        start_game=0
        myPlain=MyPLAIN()
        enemys.clear()
        dead=False
        crash_enemy=0
        round=0
        enemy_position.clear()
        boss_battle=0
        firecheck=0
        boss_count=360
        boss_bgm.stop()
        now_boss=1
        lightcheck=0
    clock.tick(60)