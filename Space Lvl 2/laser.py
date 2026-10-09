import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, position, speed, screen_height, laser_type="enemy"):
        super().__init__()
        self.speed = speed
        self.screen_height = screen_height
        self.laser_type = laser_type

        if self.laser_type == "player":
            self.image = pygame.Surface((8, 24), pygame.SRCALPHA)

            pygame.draw.rect(self.image, (0, 255, 255), (0, 0, 8, 24), border_radius=4)

            pygame.draw.rect(self.image, (255, 255, 255), (2, 2, 4, 20), border_radius=3)

        else:
            self.image = pygame.Surface((4, 15), pygame.SRCALPHA)
            pygame.draw.rect(self.image, (243, 216, 63), (0, 0, 4, 15), border_radius=2)

        self.rect = self.image.get_rect(center=position)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y > self.screen_height + 15 or self.rect.y < -30:
            self.kill()