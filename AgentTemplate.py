import pygame
from math import sin, cos, radians

class AgentTemplate():
    def __init__ (self, im = pygame.image.load("playerSprites\\player1.png").convert_alpha(), pos = [200,100], rot = 180):
        self.im = im
        self.pos = pos
        self.speed = 0.1
        self.rot = rot
        self.rotspeed = 0.1
        self.size = 35

    def draw(self, surf):
        # roterer bildet og setter riktig størrelse
        ima = pygame.transform.rotozoom(self.im, self.rot, self.size/self.im.get_height())
        # printer bildet sentrert
        surf.blit(ima, ima.get_rect(center = self.pos))

    def move(self, dir = 0):
        # passer på at dir ikke er mer enn 1 eller mindre enn -1
        dir = min(1, max(-1, dir))
        
        """ hvis vi trenger dette
        # beveger seg i retningen du ser og ikke går ut av rammen

        if self.size/2 <= self.pos[0] + sin(radians(self.rot))*self.speed*dir <= width-self.size/2:
            self.pos[0] += sin(radians(self.rot))*self.speed*dir
        if self.size/2 <= self.pos[1] + cos(radians(self.rot))*self.speed*dir <= height-self.size/2:
            self.pos[1] += cos(radians(self.rot))*self.speed*dir
        """
        # beveger seg i retningen du ser
        self.pos[0] += sin(radians(self.rot))*self.speed*dir
        self.pos[1] += cos(radians(self.rot))*self.speed*dir
    
    def rotate(self, dir = 1):
        # passer på at dir ikke er mer enn 1 eller mindre enn -1
        dir = min(1, max(-1, dir))

        self.rot = (self.rot+dir*self.rotspeed)%360
