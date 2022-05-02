class Settings:
    """A class to store all settings for alien invasion."""


    def __init__(self) -> None:
        """Initialize the game's settings."""
        # screen settings.
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5