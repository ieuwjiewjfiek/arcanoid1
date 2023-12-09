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
#font = font.SysFont('Arial',50)
#win = font.render('YOU WIN!', True,(255, 0, 0))
#lose = font.render('YOU LOSE!', True,(255, 0, 0))


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
        if keys_pressed[K_RIGHT] and self.rect.x < 300:
            self.rect.x += self.speed
#class Enemy(GameSprite):
#    def update(self):
#        self.rect.y += self.speed 
#        global lost
#        if self.rect.y >= 500:
#            self.rect.y = 0
#            self.rect.x = randint(20,600)
#            lost += 1

#class Bullet(GameSprite):
#    def update(self):
#        self.rect.y -= self.speed 
#        if self.rect.y <= 0:
#            self.kill()
#bullets = sprite.Group()
#monsters = sprite.Group()
#asteroids = sprite.Group()
#for i in range(5):
#    monster = Enemy('enemy.png', randint(20,600), 0, randint(1,2), 60, 60)               
#    monsters.add(monster)
#for c in range(2):
#    asteroid = Enemy('asteroid.png', randint(20,600), 0, randint(1,2), 50, 50)
#    asteroids.add(asteroid)

player = Player('racetka.png', 250, 400, 6, 150, 60)
ball = GameSprite('ball.png',300, 180, 13,60, 60)

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

        if ball.rect.x > 430 or ball.rect.x < 0:
            speed_x *= -1
        if sprite.collide_rect(player, ball) :
            speed_x *= -1 
        if ball.rect.y > 810 :
            finish = True


    display. update()
    clock.tick(FPS)