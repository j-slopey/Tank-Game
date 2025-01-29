#Author: James Slopey (2021)


from tkinter import *
import random
import time

# Template for class that controls the bullet canvas object
#  this is for only one bullet
#  the bullet has nothing to do with the act of shooting

class Bullet:
    def __init__(self, x, y, direction, canvas):
        # Parameters x,y are the starting location of the bullet

        #  (the location of the tank)
        self.canvas = canvas
        self.bulletr = PhotoImage(file = './images/shellr.gif')
        self.bulletd = PhotoImage(file = './images/shelld.gif')
        self.bulletL = PhotoImage(file = './images/shellL.gif')
        self.bulletu = PhotoImage(file = './images/shellu.gif')


        if direction == 'up':
            self.bullet = self.canvas.create_image(x,y+10, image = self.bulletu)
        if direction == 'down':
            self.bullet = self.canvas.create_image(x,y-10, image = self.bulletd)
        if direction == 'left':
            self.bullet = self.canvas.create_image(x-10,y, image = self.bulletL)
        if direction == 'right':
            self.bullet = self.canvas.create_image(x+10,y, image = self.bulletr)


        # Parameter direction is which direction does the bullet need to go
        self.bulletspeed = 20
        self.direction = direction
        self.tankplace = [x,y]
        self.removed = False



        # Set the speed and direction of the bullet in the init
        #  (that never changes)
    
    def move(self):
        # This move method will be called from the tank main class
        # If the canvas object has been deleted don't try to move it
        if self.removed:
            return
        # move the bullet
        if self.direction == 'up':
            self.canvas.move(self.bullet, 0, -self.bulletspeed)
        if self.direction == 'down':
            self.canvas.move(self.bullet, 0, self.bulletspeed)
        if self.direction == 'left':
            self.canvas.move(self.bullet, -self.bulletspeed, 0)
        if self.direction == 'right':
            self.canvas.move(self.bullet, self.bulletspeed, 0)

        self.bulletloc = self.canvas.coords(self.bullet)

    def getLoc(self):
        #  Returns the current location of the bullet
        xy = self.canvas.coords(self.bullet)
        return xy

        
    def checkOutOfBounds(self):
        bulletpos = self.canvas.coords(self.bullet)
        if bulletpos[0] < 10 or bulletpos[0] > 1395 or bulletpos[1] < 10 or bulletpos[1] > 895:
            return True
        return False




    

