import pygame
from pygame.locals import *
import random
import math

pygame.init()

# Create game window
game_width = 800
game_height = 400
size = (game_width, game_height)
game = pygame.display.set_mode(size)
pygame.display.set_caption('Endless Runner')

# Game variables
score = 0
speed = 3

class Player(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.height = 150
        self.x = 25
        self.y = game_height - self.height
        self.action = 'Running'
        self.health = 3

        # Load running sprite
        self.running_sprites = []
        self.running_sprite_index = 0
        for i in range(10):
            running_sprite = pygame.image.load(f'jun18 2D Rnner/images/running/run{i}.png').convert_alpha()
            scale = self.height / running_sprite.get_height()
            new_width = running_sprite.get_width() * scale
            new_height = running_sprite.get_height() * scale
            running_sprite = pygame.transform.scale(running_sprite, (new_width, new_height))
            self.running_sprites.append(running_sprite)

        # Load jumping sprite
        self.jumping_sprites = []
        self.jumping_sprite_index = 0
        for i in range(10):
            jumping_sprite = pygame.image.load(f'jun18 2D Rnner/images/jumping/jump{i}.png').convert_alpha()
            scale = self.height / jumping_sprite.get_height()
            new_width = jumping_sprite.get_width() * scale
            new_height = jumping_sprite.get_height() * scale
            jumping_sprite = pygame.transform.scale(jumping_sprite, (new_width, new_height))
            self.jumping_sprites.append(jumping_sprite)

        # Initial sprites rect
        self.rect = self.running_sprites[self.running_sprite_index].get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        # Invulnerability time of wounded player
        self.invincibility_frame = 0

    def draw(self):
        '''Draw the sprite based on the character action and index'''

        if self.action == 'Running':
            running_sprite = self.running_sprites[int(self.running_sprite_index)]

            # Add invinvicibility effect when hurt
            if self.invincibility_frame > 0:
                self.invincibility_frame -= 1
            if self.invincibility_frame % 10 == 0:
                game.blit(running_sprite, (self.x, self.y))

        elif self.action == 'Jumping' or self.action == 'Landing':
            jumping_sprite = self.jumping_sprites[int(self.jumping_sprite_index)]

            # Add invicibility effect when hurt 
            if self.invincibility_frame > 0:
                self.invincibility_frame -= 1
            if self.invincibility_frame % 10 == 0:
                game.blit(jumping_sprite, (self.x, self.y))

    def update(self):
        '''Update sprite index'''
        '''Update y position'''

        if self.action == 'Running':

            # Increase sprite index by 0.2
            # Now only 5 shots are needed
            self.running_sprite_index += 0.2

            # Go back to index after the last sprite image is drawn
            if self.running_sprite_index >= len(self.running_sprites):
                self.running_sprite_index = 0

            # Update rect
            self.rect = self.running_sprites[int(self.running_sprite_index)].get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

            # Update the mask for collision detection
            self.mask = pygame.mask.from_surface(self.running_sprites[int(self.running_sprite_index)])

        elif self.action == 'Jumping' or self.action == 'Landing':
            
            # Increase sprite index by 0.2
            # Now only 5 shots are needed
            self.jumping_sprite_index += 0.2

            # Go back to index after the last sprite image is drawn
            if self.jumping_sprite_index >= len(self.jumping_sprites):
                self.jumping_sprite_index = 0

            # Change position when jumping and when landing
            if self.action == 'Jumping':
                self.y -= 2

                # Change to landing when peak of jump is reached
                if self.y <= game_height - self.height * 1.5:
                    self.action = 'Landing'
            
            elif self.action == 'Landing':
                self.y += 2

                # Change to runnng when character toucher the ground
                if self.y == game_height - self.height:
                    self.action = 'Running'

            # Update rect
            self.rect = self.jumping_sprites[int(self.jumping_sprite_index)].get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

            # Update maskfor collision detected
            self.mask = pygame.mask.from_surface(self.jumping_sprites[int(self.jumping_sprite_index)])

    def jump(self):
        '''Make player go ot jump action when not already jumping or landing'''
        if self.action not in ['Jumping', 'Landing']:
            self.action = 'Jumping'

class Obstacle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Load obstacle image
        self.obstacle_images = []
        for image_name in ['rock1', 'rock2', 'rock3', 'spikes']:
            image = pygame.image.load(f'jun18 2D Rnner/images/obstacles//{image_name}.png').convert_alpha()
            scale = 50 / image.get_width()
            new_width = image.get_width() * scale
            new_height = image.get_height() * scale
            image = pygame.transform.scale(image, (new_width, new_height))
            self.obstacle_images.append(image)

        # Assing rand image
        self.image = random.choice(self.obstacle_images)

        # Position obstacle on right screen
        self.x = game_width
        self.y = game_height - self.image.get_height()

        # Set the initial rect
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        game.blit(self.image, (self.x, self.y))

    def update(self):
        '''Move obstacle to left'''

        # Move left
        self.x -= speed

        # Update the rect
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        # Update the mask for collision detection
        self.mask = pygame.mask.from_surface(self.image)

    def reset(self):
        '''Assign a new image and reset back to original position'''

        self.image = random.choice(self.obstacle_images)
        self.x = game_width
        self.y = game_height - self.image.get_height()

# Set sky image
sky = pygame.image.load('jun18 2D Rnner/images/bg/sky.png').convert_alpha()
num_bg_tiles = math.ceil(game_width / sky.get_width()) + 1

# Set parallax background
bgs = []
bgs.append(pygame.image.load('jun18 2D Rnner/images/bg/mountains.png').convert_alpha())
bgs.append(pygame.image.load('jun18 2D Rnner/images/bg/trees.png').convert_alpha())
bgs.append(pygame.image.load('jun18 2D Rnner/images/bg/bushes.png').convert_alpha())

# for the parallax effect, determine how much each layer will scroll
parralax = []
for x in range(len(bgs)):
    parralax.append(0)

# Create player
player = Player()

# Create obstacle
obstacle_group = pygame.sprite.Group()
obstacle = Obstacle()
obstacle_group.add(obstacle)

# Load helth image
heart_sprites = []
heart_sprite_index = 0
for i in range(8):
    heart_sprite = pygame.image.load(f'jun18 2D Rnner/images/heart/heart{i}.png').convert_alpha()
    scale = 30 / heart_sprite.get_height()
    new_width = heart_sprite.get_width() * scale
    new_height = heart_sprite.get_height() * scale
    heart_sprite = pygame.transform.scale(heart_sprite, (new_width, new_height))
    heart_sprites.append(heart_sprite)

# Game loop
clock = pygame.time.Clock()
FPS = 90
Quit = False
while not Quit:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Quit = True

        # Press SPACE to jump
        elif event.type == KEYDOWN and event.key == K_SPACE:
            player.jump()

    # Draw sky
    for i in range(num_bg_tiles):
        game.blit(sky, (i * sky.get_width(), 0))

    # Draw background layer
    for i in range(len(bgs)):

        bg = bgs[i]

        for j in range(num_bg_tiles):
            game.blit(bg, (j * bg.get_width() + parralax[i], 0))

    # Update layers scroll
    for i in range(len(parralax)):

        # Faster top layer
        parralax[i] -= i + 1

        if abs(parralax[i]) > bgs[i].get_width():
            parralax[i] = 0

    # Draw player
    player.draw()

    # Update sprites and position
    player.update()

    # Draw obstagle
    obstacle.draw()

    # Update obstacle pos
    obstacle.update()

    # Add to score and reset the obstacle when it goes off screen
    if obstacle.x < obstacle.image.get_width() * -1:

        score += 1
        obstacle.reset()

        # increase the speed after clearing 2 obstacles
        # but the max it can go up to is 10
        if score % 2 == 0 and speed < 10:
            speed += 1

    # Check if player touch obstacle
    if pygame.sprite.spritecollide(player, obstacle_group, True, pygame.sprite.collide_mask):
        player.health -= 1
        player.invincibility_frame = 3

        # Remove obstacle and replace with a new one
        obstacle_group.remove(obstacle)
        obstacle = Obstacle()
        obstacle_group.add(obstacle)

    # Display a heart per remeining health
    for life in range(player.health):
        heart_sprite = heart_sprites[int(heart_sprite_index)]
        x_pos = 10 + life * (heart_sprite.get_width() + 10)
        y_pos = 10
        game.blit(heart_sprite, (x_pos, y_pos))
    
    # Increment the index for the next hearth sprite
    # Use 0.1 to make the sprite change after 10 frames 
    heart_sprite_index += 0.1

    # Set index back to 0 after the last heart sprite is drawn
    if heart_sprite_index >= len(heart_sprites):
        heart_sprite_index = 0

    # Display the score
    black = (0, 0, 0)
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render(f'Score: {score}', True, black)
    text_rect = text.get_rect()
    text_rect.center = (game_width -50, 20)
    game.blit(text, text_rect)

    pygame.display.update()

    # Game over
    gameover = player.health == 0
    while gameover and not Quit:

        # Display game over message
        red = (255, 0, 0)
        pygame.draw.rect(game, red, (0, 50, game_width, 100))
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render('Game over. Play again? (Enter Y or N)', True, black)
        text_rect = text.get_rect()
        text_rect.center = (game_width / 2, 100)
        game.blit(text, text_rect)

        for event in pygame.event.get():
            
            if event.type == QUIT:
                Quit = True

            # Get the players input
            if event.type == KEYDOWN:
                if event.key == K_y:
                    # Reset the game
                    gameover = False
                    speed = 3
                    score = 0
                    player = Player()
                    obstacle= Obstacle()
                    obstacle_group.empty()
                    obstacle_group.add(obstacle)
                elif event.key == K_n:
                    Quit = True

        pygame.display.update()

pygame.quit()