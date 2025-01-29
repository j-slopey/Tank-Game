#Author: James Slopey (2021)


from tkinter import *
import random
import time

class Target:
    def __init__(self, canvas):
        # Pass a reference to the canvas from the Tank main class
        self.canvas = canvas
        

        
        # Create the target and explosion images and randomly place the target
        self.melon = PhotoImage(file = './images/melon.gif')
        self.popped = PhotoImage(file = './images/popped.gif')
        x = random.randint(50,950)
        y = random.randint(50,650)
        self.target = self.canvas.create_image(x,y,image = self.melon)
        
        # Initialize variables
        #   Move amounts
        self.x = random.randrange(-5,5)
        self.y = random.randrange(-5,5)
        #   Starting time
        self.starttime = time.time()
        #   Boolean variable to keep track of status
        self.exploding = False
        self.removed = False
        
    def getLoc(self):
        # Return the location of the target when requested
        xy = self.canvas.coords(self.target)
        return xy

    def getRemoved(self):
        # Return the removed status
        return self.removed
    
    def move(self):
        # If the target has been deleted don't try to move it
        if self.removed:
            return
        # Change direction of target if it hits the side
        xy = self.canvas.coords(self.target)
        if xy[0] < 50:
            self.x = random.randrange(1,5)
            self.y = random.randrange(-5,5)
        if xy[0] > 950:
            self.x = random.randrange(-5,-1)
            self.y = random.randrange(-5,5)
        if xy[1] < 50:
            self.x = random.randrange(-5,5)
            self.y = random.randrange(1,3)
        if xy[1] > 850:
            self.x = random.randrange(-5,5)
            self.y = random.randrange(-5,-1)
        
        
                                      
        
        # Move the targer
        self.canvas.move(self.target,self.x,self.y)
        # If the target is exploding then delete the target after 2 seconds
        #  (remember to keep track of target status)
        if self.exploding:
            self.x = 0
            self.y = 0
            if time.time() - self.starttime > 2:
                self.canvas.delete(self.target)
                self.removed = True

                
    def explode(self):
        # The target has been informed to explode
        #  (remember to keep track of target status)
        if self.exploding == False:
            self.exploding = True
            self.starttime = time.time()
            self.canvas.itemconfig(self.target, image = self.popped)
        
        


