import os
import sys
import pygame as pg
import random


WIDTH, HEIGHT = 1100, 650
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 0.9)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    clock = pg.time.Clock()
    tmr = 0
    bb_img=pg.Surface((20, 20))
    bb_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)
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
    def check_bound(rct:pg.Rect) -> tuple[bool,bool]: 
        yoko,tate=True,True
        if 0 > rct.left or rct.right > WIDTH:
            yoko=False
        if 0 > rct.top or rct.bottom > HEIGHT:
            tate=False
        return yoko,tate

    while True:
        
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
        bb_rct.move_ip(vx,vy)
        screen.blit(bb_img, bb_rct)
        if kk_rct.colliderect(bb_rct):
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
