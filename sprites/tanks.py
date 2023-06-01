import pygame


class Tank:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/tank.svg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.speed = 3
        self.rect.centerx = pygame.display.get_surface().get_size()[0]/2
        self.rect.centery = pygame.display.get_surface().get_size()[1] - 25
        self.left, self.right, self.up, self.down = False, False, False, False
        self.rotated_up, self.rotated_down, self.rotated_left, self.rotated_right = True, False, False, False

    def output(self):
        if self.left:
            if self.rect.centerx % 4 == 0:
                self.image = pygame.image.load('images/tank_l.svg')
            else:
                self.image = pygame.image.load('images/tank_alt_l.svg')
        if self.right:
            if self.rect.centerx % 4 == 0:
                self.image = pygame.image.load('images/tank_r.svg')
            else:
                self.image = pygame.image.load('images/tank_alt_r.svg')
        if self.down:
            if self.rect.centery % 4 == 0:
                self.image = pygame.image.load('images/tank_d.svg')
            else:
                self.image = pygame.image.load('images/tank_alt_d.svg')
        if self.up:
            if self.rect.centery % 4 == 0:
                self.image = pygame.image.load('images/tank.svg')
            else:
                self.image = pygame.image.load('images/tank_alt.svg')
        # image = pygame.transform.scale(self.image, (50, 50))
        self.screen.blit(self.image, self.rect)

    def update_position(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.left = True
                    self.right, self.up, self.down = False, False, False
                elif event.key == pygame.K_RIGHT:
                    self.right = True
                    self.left, self.up, self.down = False, False, False
                elif event.key == pygame.K_UP:
                    self.up = True
                    self.right, self.left, self.down = False, False, False
                elif event.key == pygame.K_DOWN:
                    self.down = True
                    self.up, self.left, self.right = False, False, False
            elif event.type == pygame.KEYUP:
                self.left, self.right, self.up, self.down = False, False, False, False

        disp_x, disp_y = pygame.display.get_surface().get_size()
        if self.left and self.rect.left > 0:
            self.rect.centerx -= self.speed
        if self.right and self.rect.right < disp_x:
            self.rect.centerx += self.speed
        elif self.up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= self.speed
        elif self.down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.speed
