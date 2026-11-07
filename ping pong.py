# import
from pygame import *

# game scene/window
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height)) # create window

bg_color = (200, 255, 255)
window.fill(bg_color) # fill bg color

class GameSprite(sprite.Sprite):
    # constructor
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # show image
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    # left platform
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5: # up
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80: # down
            self.rect.y += self.speed

    # right platform
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5: # up
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80: # down
            self.rect.y += self.speed
            
# objects
racket1 = Player('shape.png', 30, 200, 4, 50, 150)
racket2 = Player('shape.png', 520, 200, 4, 50, 150)
ball = GameSprite('tennis.png', 200, 200, 4, 50, 50)

# game loop
game = True
clock = time.Clock()

finish = False

# ball speed
speed_x = 3
speed_y = 3

# text
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

while game:
    # close
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(bg_color) # fill background color

        # racket movement
        racket1.update_l()
        racket2.update_r()

        # ball movement
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        # ball-racket
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            
    # ball - screen edges (top-bottom)
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
            
    # ball di belakang racket 1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        # ball di belakang racket 2
        if ball.rect.x > win_width-50:
            finish = True
            window.blit(lose2, (200, 200))    
        
    # show sprites
    racket1.reset()
    racket2.reset()
    ball.reset()

    display.update()
    clock.tick(60)