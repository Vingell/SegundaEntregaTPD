from math import radians
from math import sin
import pygame
from pygame import *

class projectileMotion:
        
    def _init_(self, g = -100, velocity = 150, angle = 45):
        self.Vel = velocity
        self.angle = angle
        self.g = g           
        self.yo = 0.
        self.Y = 0.
        self.deltaY  = 0.
        self.tempTimer = 0.

    def start(self, y0):
        self.tempTimer = 0
        self.Y = y0
        self.yo = y0
        self.inProcess = True
        self.deltaY = 0

    def update(self, totalElapsedTime):
        tempY = self.Y
        ##self.T = totalElapsedTime
                
        ##self.Y = self.yo + self.Vel * math.sin(math.radians(self.angle)) * self.T - (0.5) * self.g * self.T ** 2
        self.Y =  self.yo + (self.Vel * sin(radians(self.angle)) * self.tempTimer) - ((0.5) * self.g * self.tempTimer * self.tempTimer)
        #print str("Y0  : " + str(self.yo))
        #print str("Y  : " + str(self.Y))
            
        self.tempTimer += 0.2
        #print str("tempTimer  : " + str(self.tempTimer))
        self.deltaY = self.Y - tempY
        #print str("deltaY  : " + str(self.deltaY))
        #print "-------------"

    def stop(self):
        self.inProcess = False
        self.deltaY = 0
        self.Y = 0
        self.tempTimer = 0

    tempTimer = 0.0

    yo = 0.0
    Y = 0.0
    deltaY = 0.0

    g = float()
    Vel = float()
    angle = float()

    T = 0.0
    inProcess = bool()

        

