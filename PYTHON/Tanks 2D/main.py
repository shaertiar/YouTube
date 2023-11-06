import pygame as pg

pg.init()

# Create window
window_width, window_height = 800, 600
window = pg.display.set_mode((window_width, window_height))

# Create class
class Tank:
    def __init__(self, color, px, py, direct, key_list):
        objects.append(self)

        self.type = 'tank'
        self.color = color
        self.rect = pg.Rect(px, py, tile, tile)
        self.direct = direct
        self.move_speed = 2
        self.hp = 5

        self.bullet_speed = 5
        self.bullet_damage = 1
        self.shoot_timer = 0
        self.shoot_delay = fps

        self.key_up = key_list[0]
        self.key_left = key_list[1]
        self.key_down = key_list[2]
        self.key_right = key_list[3]
        self.key_shoot = key_list[4]

    def update(self):
        if keys[self.key_up]:
            self.rect.y -= self.move_speed
            self.direct = 0

        elif keys[self.key_left]:
            self.rect.x -= self.move_speed
            self.direct = 1

        elif keys[self.key_down]:
            self.rect.y += self.move_speed
            self.direct = 2

        elif keys[self.key_right]:
            self.rect.x += self.move_speed
            self.direct = 3

        elif keys[self.key_shoot]:
            if self.shoot_timer == 0:
                dx = directs[self.direct][0] * self.bullet_speed
                dy = directs[self.direct][1] * self.bullet_speed
                Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bullet_damage)

                self.shoot_timer += self.shoot_delay

        if self.shoot_timer > 0:
            self.shoot_timer -= 1

    def draw(self):
        pg.draw.rect(window, self.color, self.rect)

        x = self.rect.centerx + directs[self.direct][0] * 30
        y = self.rect.centery + directs[self.direct][1] * 30
        pg.draw.line(window, (255, 255, 255), self.rect.center, (x, y))

class Bullet:
    def __init__(self, parent, px, py, dx, dy, damage):
        bullets.append(self)

        self.parent = parent
        self.damage = damage
        self.px = px
        self.py = py
        self.dx = dx
        self.dy = dy

    def update(self):
        self.px += self.dx
        self.py += self.dy

        if ((self.px > 0) or (self.px > window_width)) or ((self.py > 0) or (self.py > window_height)):
            bullets.remove(self)
        else:
            for obj in objects:
                if obj != self.parent:
                    if obj.rect.collidepoint(self.px, self.py):
                        obj.damage(self.damage)
                        bullets.remove(self)
                        breakdads

    def damage(self, value):
        self.hp -= value

        if self.hp <= 0:
            objects.remove(self)
            print(f'{self.color} dead')

    def draw(self):
        pg.draw.circle(window, (255, 255, 0), (self.px, self.py), 2)

# Settings
fps = 60

Clock = pg.time.Clock()

tile = 32

objects = []
bullets = []

# Variables
Tank((0, 0, 255), 100, 275, 0, (pg.K_w, pg.K_a, pg.K_s, pg.K_d, pg.K_LCTRL))
Tank((255, 0, 0), 650, 275, 0, (pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT, pg.K_RCTRL))

directs = [[0, -1], [-1, 0], [0, 1], [1, 0]]

# Main loop
play = True
while play:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            play = False

    keys = pg.key.get_pressed()

    window.fill((0, 0, 0))

    for bullet in bullets:
        bullet.update()
        bullet.draw()

    for obj in objects:
        obj.update()
        obj.draw()

    pg.display.update()
    Clock.tick(fps)

pg.quit()