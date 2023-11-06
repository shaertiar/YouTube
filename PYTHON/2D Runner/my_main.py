import pygame as pg
import random
import math

pg.init()

window_width = 800
window_height = 400
game = pg.display.set_mode((window_width, window_height))

pg.display.set_caption('Endless Runner')

score = 0
speed = 3
max_score = 0

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)  

        self.height = 150
        self.x = 25
        self.y = window_height - self.height
        self.action = 'Running'
        self.health = 3

        self.running_sprites = []
        self.running_sprite_index = 0
        for i in range(10):
            running_sprite = pg.image.load(f'images/running/run{i}.png').convert_alpha()
            scale = self.height / running_sprite.get_height()
            new_width = running_sprite.get_width() * scale
            new_height = running_sprite.get_height() * scale
            running_sprite = pg.transform.scale(running_sprite, (new_width, new_height))
            self.running_sprites.append(running_sprite)

        self.jumping_sprites = []
        self.jumping_sprite_index = 0
        for i in range(10):
            jumping_sprite = pg.image.load(f'images/jumping/jump{i}.png').convert_alpha()
            scale = self.height / jumping_sprite.get_height()
            new_width = jumping_sprite.get_width() * scale
            new_height = jumping_sprite.get_height() * scale
            jumping_sprite = pg.transform.scale(jumping_sprite, (new_width, new_height))
            self.jumping_sprites.append(jumping_sprite)

        self.rect = self.running_sprites[self.running_sprite_index].get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.invincibility_frame = 0

    def draw(self):
        if self.action == 'Running':
            running_sprite = self.running_sprites[int(self.running_sprite_index)]

            if self.invincibility_frame > 0:
                self.invincibility_frame -= 1

            if self.invincibility_frame % 10 == 0:
                game.blit(running_sprite, (self.x, self.y))

        elif self.action == 'Jumping' or self.action == 'Landing':
            jumping_sprite = self.jumping_sprites[int(self.jumping_sprite_index)]

            if self.invincibility_frame > 0:
                self.invincibility_frame -= 1

            if self.invincibility_frame % 10 == 0:
                game.blit(jumping_sprite, (self.x, self.y))

    def update(self):
        if self.action == 'Running':
            self.running_sprite_index += 0.2

            if self.running_sprite_index >= len(self.running_sprites):
                self.running_sprite_index = 0

            self.rect = self.running_sprites[int(self.running_sprite_index)].get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

            self.mask = pg.mask.from_surface(self.running_sprites[int(self.running_sprite_index)])

        elif self.action == 'Jumping' or self.action == 'Landing':
            self.jumping_sprite_index += 0.2

            if self.jumping_sprite_index >= len(self.jumping_sprites):
                self.jumping_sprite_index = 0

            if self.action == 'Jumping':
                self.y -= 2

                if self.y <= window_height - self.height * 1.5:
                    self.action = 'Landing'
            
            elif self.action == 'Landing':
                self.y += 2

                if self.y == window_height - self.height:
                    self.action = 'Running'

            self.rect = self.jumping_sprites[int(self.jumping_sprite_index)].get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

            self.mask = pg.mask.from_surface(self.jumping_sprites[int(self.jumping_sprite_index)])

    def jump(self):
        if self.action not in ['Jumping', 'Landing']:
            self.action = 'Jumping'

class Obstacle(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.obstacle_images = []
        for image_name in ['rock1', 'rock2', 'rock3', 'spikes']:
            image = pg.image.load(f'images/obstacles//{image_name}.png').convert_alpha()
            scale = 50 / image.get_width()
            new_width = image.get_width() * scale
            new_height = image.get_height() * scale
            image = pg.transform.scale(image, (new_width, new_height))
            self.obstacle_images.append(image)

        self.image = random.choice(self.obstacle_images)

        self.x = window_width
        self.y = window_height - self.image.get_height()

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        game.blit(self.image, (self.x, self.y))

    def update(self):
        self.x -= speed

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.mask = pg.mask.from_surface(self.image)

    def reset(self):
        self.image = random.choice(self.obstacle_images)
        self.x = window_width
        self.y = window_height - self.image.get_height()

sky = pg.image.load('images/bg/sky.png').convert_alpha()
num_bg_tiles = math.ceil(window_width / sky.get_width()) + 1

bgs = []
bgs.append(pg.image.load('images/bg/mountains.png').convert_alpha())
bgs.append(pg.image.load('images/bg/trees.png').convert_alpha())
bgs.append(pg.image.load('images/bg/bushes.png').convert_alpha())

parralax = []
for x in range(len(bgs)):
    parralax.append(0)

player = Player()

obstacle_group = pg.sprite.Group()
obstacle = Obstacle()
obstacle_group.add(obstacle)

heart_sprites = []
heart_sprite_index = 0

for i in range(8):
    heart_sprite = pg.image.load(f'images/heart/heart{i}.png').convert_alpha()
    scale = 30 / heart_sprite.get_height()
    new_width = heart_sprite.get_width() * scale
    new_height = heart_sprite.get_height() * scale
    heart_sprite = pg.transform.scale(heart_sprite, (new_width, new_height))
    heart_sprites.append(heart_sprite)

clock = pg.time.Clock()
FPS = 90
Quit = False

while not Quit:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Quit = True

        # elif event.type == pg.KEYDOWN:
            # if event.key == pg.K_SPACE:
                # player.jump()
        
        elif event.type in [pg.KEYDOWN, pg.MOUSEBUTTONDOWN]:
            player.jump()

            # elif event.key == pg.K_UP:
            #     window_width += 100
            # elif event.key == pg.K_DOWN:
            #     window_width -= 100
            # yy  game = pg.display.set_mode((window_width, window_height))

    for i in range(num_bg_tiles):
        game.blit(sky, (i * sky.get_width(), 0))

    for i in range(len(bgs)):
        bg = bgs[i]

        for j in range(num_bg_tiles):
            game.blit(bg, (j * bg.get_width() + parralax[i], 0))

    for i in range(len(parralax)):
        parralax[i] -= i + 1

        if abs(parralax[i]) > bgs[i].get_width():
            parralax[i] = 0

    player.draw()
    player.update()

    obstacle.draw()
    obstacle.update()

    if obstacle.x < obstacle.image.get_width() * -1:
        score += 1
        obstacle.reset()

        if score % 2 == 0 and speed < 10:
            speed += 1

    if pg.sprite.spritecollide(player, obstacle_group, True, pg.sprite.collide_mask):
        player.health -= 1
        player.invincibility_frame = 3

        obstacle_group.remove(obstacle)
        obstacle = Obstacle()
        obstacle_group.add(obstacle)

    for life in range(player.health):
        heart_sprite = heart_sprites[int(heart_sprite_index)]
        x_pos = 10 + life * (heart_sprite.get_width() + 10)
        y_pos = 10
        game.blit(heart_sprite, (x_pos, y_pos))
    
    heart_sprite_index += 0.1

    if heart_sprite_index >= len(heart_sprites):
        heart_sprite_index = 0

    font = pg.font.Font(pg.font.get_default_font(), 16)
    text = font.render(f'Score: {score}', True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (window_width -50, 20)
    game.blit(text, text_rect)

    gameover = player.health == 0

    while gameover and not Quit:
        if score > max_score: 
            max_score = score
        pg.draw.rect(game, (255, 0, 0), (0, 50, window_width, 100))
        font = pg.font.Font(pg.font.get_default_font(), 16)
        text = font.render(f'Game over. Play again? (Enter Y or N).', True, (0, 0, 0))
        text2 = font.render(f'Your score: {score}, Max score: {max_score}.', True, (0, 0, 0))
        text_rect = text.get_rect()
        text2_rect = text2.get_rect()
        text_rect.center = (window_width / 2, 100)
        text2_rect.center = (window_width / 2, 120)
        game.blit(text, text_rect)
        game.blit(text2, text2_rect)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                Quit = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_y:
                    gameover = False
                    speed = 3
                    score = 0
                    player = Player()
                    obstacle= Obstacle()
                    obstacle_group.empty()
                    obstacle_group.add(obstacle)

                elif event.key == pg.K_n:
                    Quit = True

        pg.display.update()

    pg.display.update()

    clock.tick(FPS)

pg.quit()