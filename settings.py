class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        self.BLOCKSIZE = 10
        self.WINDOW_WIDTH = 800
        self.WIDTH = int(self.WINDOW_WIDTH/self.BLOCKSIZE)
        self.WINDOW_HEIGHT = 600
        self.HEIGHT = int(self.WINDOW_HEIGHT/self.BLOCKSIZE)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255,255,255)
        self.REDS =  [(x,0,0) for x in range(20,220,5)]