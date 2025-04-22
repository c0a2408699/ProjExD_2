import os
import sys
import random
import time
import pygame as pg



WIDTH, HEIGHT = 1100, 650
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    font = pg.font.Font(None, 80)
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))

    #ゲームオーバー画面
    gameover = pg.Surface((WIDTH, HEIGHT))
    gameover.fill(pg.Color("BLACK"))
    txt = font.render("GAME OVER", False, (255, 255, 255))
    gameover.blit(txt, [WIDTH/2-180,HEIGHT/2-80])
    gameover.set_alpha(220)
    go1_img = pg.image.load("fig/8.png") 
    go2_img = pg.image.load("fig/8.png") 
    gameover.blit(go1_img,[WIDTH/2-260,HEIGHT/2-90])
    gameover.blit(go2_img,[WIDTH/2+200,HEIGHT/2-90])

    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 0.9)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    clock = pg.time.Clock()
    tmr = 0
    bb_size=[20,20]
    bb_img=pg.Surface((bb_size[0], bb_size[1]))
    bb_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bb_img, (255, 0, 0), (bb_size[0]/2, bb_size[1]/2), 10)
    bb_rct=random.randint(0,WIDTH),random.randint(0,HEIGHT)
    bb_rct=bb_img.get_rect()
    vx=5
    vy=5
    DELTA={
            pg.K_UP:(0,-5),
            pg.K_DOWN:(0,5),
            pg.K_LEFT:(-5,0),
            pg.K_RIGHT:(5,0)
        }
    def timeevent(time,vx,vy):
         if tmr<1200:
            vx+=vx*0.001
            vy+=vy*0.001
            return vx,vy
    def timeevent(time,vx,vy):
         if tmr<1200:
            vx+=vx*0.001
            vy+=vy*0.001
            return vx,vy
    #画面端検知
    def check_bound(rct:pg.Rect) -> tuple[bool,bool]: 
        yoko,tate=True,True
        if 0 > rct.left or rct.right > WIDTH:
            yoko=False
        if 0 > rct.top or rct.bottom > HEIGHT:
            tate=False
        return yoko,tate
    bb_rct.center=[random.randint(10,WIDTH),random.randint(10,HEIGHT)]
    r=0
    while True:
        
        bb_img.set_colorkey((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0]) 

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for key,mv in DELTA.items():
            if key_lst[key]:
                sum_mv[0]+=mv[0]
                sum_mv[1]+=mv[1]
        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct)!=(True,True):
            kk_rct.move_ip(-sum_mv[0],-sum_mv[1])
        screen.blit(kk_img, kk_rct)
        #加速、巨大化
        vx,vy=timeevent(tmr,vx,vy)
            
        bb_rct.move_ip(vx,vy)
        screen.blit(bb_img, bb_rct)
        if tmr < 1200:
            r+=0.01
        bb_img = pg.Surface((20*r, 20*r))
        pg.draw.circle(bb_img, (255, 0, 0), (10*r, 10*r), 10*r)
        if kk_rct.colliderect(bb_rct):
            screen.blit(gameover,(0,0))
            pg.display.update()
            time.sleep(5)
            return
        if not check_bound(bb_rct)[0]:
            vx=vx*-1
        if not check_bound(bb_rct)[1]:
            vy=vy*-1
        
        pg.display.update()
        tmr += 1
        clock.tick(60)
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()