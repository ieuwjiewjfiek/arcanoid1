from pygame import *
from random import randint
mixer.init()
font.init()
window = display.set_mode((500, 500))
background = transform.scale(image.load('background.jpg'),(500, 500))

clock = time.Clock()
FPS = 60
#mixer.music.load('space.ogg')
#mixer.music.play()
#fire_sound = mixer.Sound('fire.ogg')
#
#lost = 0
#kill = 0
#
font = font.SysFont('Arial',50)
win = font.render('YOU WIN!', True,(255, 0, 0))
lose = font.render('YOU LOSE!', True,(255, 0, 0))


game = True
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, x_size, y_size):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (x_size, y_size))        
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.x_size = x_size
        self.y_size = y_size
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 350:
            self.rect.x += self.speed
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed 
        global lost
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = randint(20,600)
            lost += 1
xCor1 = 20
xCor2 = 40
xCor3 = 60
monsters1 = sprite.Group()
for i in range(6):
    monsterOne = Enemy('vrag.png',xCor1 ,10 ,0, 50, 50)        
    xCor1 += 80      
    monsters1.add(monsterOne)
monsters2 = sprite.Group()
for i in range(5):
    monsterTwo = Enemy('vrag.png',xCor2 ,60 ,0, 50, 50)        
    xCor2 += 90      
    monsters2.add(monsterTwo)
monsters3 = sprite.Group()
for i in range(4):
    monsterThree = Enemy('vrag.png',xCor3 ,110 ,0, 50, 50)        
    xCor3 += 100      
    monsters3.add(monsterThree)
#for c in range(2):
#    asteroid = Enemy('asteroid.png', randint(20,600), 0, randint(1,2), 50, 50)
#    asteroids.add(asteroid)

player = Player('racetka.png', 250, 450, 6, 120,30)
ball = GameSprite('ball.png',200, 100, 13,50, 50)

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
                


    if finish != True:

        
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.blit(background,(0, 0))


        player.update()
        player.reset()
        ball.reset()
        monsters1.update()
        monsters1.draw(window)
        monsters2.update()
        monsters2.draw(window)
        monsters3.update()
        monsters3.draw(window)

        if ball.rect.x < 2 or ball.rect.x > 450 :
            speed_x *= -1
        if ball.rect.y < 5:
            speed_y *= -1 
        if sprite.collide_rect(player, ball) :
            speed_y *= -1 
        if ball.rect.y > 500 :
            finish = True
            window.blit(lose, (140, 215))


    display. update()
    clock.tick(FPS)
