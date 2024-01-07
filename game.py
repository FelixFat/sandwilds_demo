import pygame
from settings import *
from player import Player
from map import *


class Game:

    def __init__(self) -> None:
        self._running = True
        self._player = None
        self._keys = []
        
    def start(self):
        pygame.init()
        pygame.display.set_caption("Sandwilds")

        self.clock = pygame.time.Clock()
        self.scene = pygame.display.set_mode((WIDTH, HIEGHT))

        self.map = Map()

    def run(self):
        while self._running:
            self._events()
            self._action()
            self._render()

            self.clock.tick(FPS)
    
    def _events(self):
        self._keys = pygame.key.get_pressed()
        self._mods = pygame.key.get_mods()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self._player is None:
                    self._player = Player(pygame.mouse.get_pos())
                    print(f"Player is created at: {self._player.get_pos()}")
                else:
                    print(f"Click! {pygame.mouse.get_pos()}")
    
    def _action(self):
        if self._player is not None:
            self._player.move(self._keys, self._mods)
    
    def _render(self):
        self.map.draw(self.scene)
        
        if self._player is not None:
            self._player.draw(self.scene)

        pygame.display.flip()

    def close(self):
        pygame.quit()