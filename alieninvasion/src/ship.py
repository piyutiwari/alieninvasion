import pygame

class Ship:
    """A class to manage the ship."""


    def __init__(self, ai_game) -> None:
        """Initialize teh ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load teh ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom centre of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for teh ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False

        self.moving_left = False

    def update(self):
        """Update ship's position based on the movement flag."""
        # update ship's x value not rect.
        if self.moving_right:
            self.x += self.settings.ship_speed
        elif self.moving_left:
            self.x -= self.settings.ship_speed


        #Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw teh ship at its current location."""
        self.screen.blit(self.image,self.rect)