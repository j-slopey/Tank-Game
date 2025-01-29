#Author: James Slopey (2021)


from tkinter import *
import random
import time
import Target
import Bullet
import math

class Tank():
    
    def __init__(self):
        # Set up the root window, frame, and canvas
        self.tk = Tk()
        self.tk.title("Tank")
        self.tk.resizable(0, 0)
        # Create the frame and initialize the grid layout manager
        frame = Frame(self.tk)
        frame.grid()
        # Create a canvas
        self.canvas = Canvas(frame, width=1400, height=900, bg = 'blanched almond')
        self.canvas.grid(row=1, column=1)
        
        self.tankr = PhotoImage( file = './images/tankr.gif')
        self.tanku = PhotoImage( file = './images/tanku.gif')
        self.tankl = PhotoImage( file = './images/tankl.gif')
        self.tankd = PhotoImage( file = './images/tankd.gif')
        
        self.tank = self.canvas.create_image(100,100, image = self.tankr)
        # Add the other widgets/set up the canvas 
        
        
        # Set up the stop button
        self.stopb = Button(frame, text="Close", command=self.endProgram)
        self.stopb.grid(row=2, column=1)
        self.stop = False
        # Initialize class variables
        self.tankspeed = 7
        self.direction = 'right'
        self.targets = []
        self.bullets = []

        for x in range(10):
            self.targets.append(Target.Target(self.canvas))
        
        self.canvas.bind_all("<KeyPress-Up>", self.up)
        self.canvas.bind_all("<KeyPress-Down>", self.down)
        self.canvas.bind_all("<KeyPress-Right>", self.right)
        self.canvas.bind_all("<KeyPress-Left>", self.left)
        self.canvas.bind_all('<KeyPress-space>',self.shoot)

    

        
    def up(self, eventdata):
        
        self.canvas.move(self.tank, 0,self.tankspeed*-1 )
        self.canvas.itemconfig(self.tank, image = self.tanku)
        self.direction = 'up'

        
    def down(self, eventdata):
         
        self.tankspeed = 7
        self.canvas.move(self.tank, 0, self.tankspeed)
        self.canvas.itemconfig(self.tank, image = self.tankd)
        self.direction = 'down'

        
    def right(self, eventdata):
        self.tankspeed = 7
        self.canvas.itemconfig(self.tank, image = self.tankr)
        self.canvas.move(self.tank, self.tankspeed, 0)
        self.direction = 'right'

    def left(self, eventdata):
        self.tankspeed = 7
        tankpos = self.canvas.coords(self.tank)
        self.canvas.itemconfig(self.tank, image = self.tankl)
        self.canvas.move(self.tank, self.tankspeed*-1, 0)
        self.direction = 'left'


    def shoot(self, eventdata):
        pos = self.canvas.coords(self.tank)
        x = pos[0]
        y = pos[1]
        self.bullets.append(Bullet.Bullet(x,y,self.direction,self.canvas))
        
    
    
    def endProgram(self):
        # Method called with stop buttion pressed
        self.stop = True

    def move(self):
        # Method called from while loop to move objects
        #  (only used if something needs to move)
        #self.canvas.move(self., self.x, self.y)
        
        for x in self.bullets:
            for y in self.targets:
                if y.getRemoved() == False and self.collision(y.getLoc(), x.getLoc()) == True:
                    y.explode()
                    self.bullets.remove(x)
            for y in self.targets:
                if y.getRemoved():
                    self.targets.remove(y)
                
            if len(self.targets) == 0:
                self.canvas.create_text(700, 450, text = "You Won!", font=("Arial","50"))
            x.move()
            if x.checkOutOfBounds():
                    self.bullets.remove(x)

        for x in self.targets:
            x.move()
            


    def collision(self, targetLocation, bulletLocation):
        x = abs(targetLocation[0] - bulletLocation[0])
        y = abs(targetLocation[1] - bulletLocation[1])
        dist = math.sqrt(x*x + y*y)
        if dist < 40:
            return True
        else:
            return False
        
            
                
        
        

    def main(self):
        # Main loop that runs the game
        while True:
            time.sleep(.03)
            self.move()
            self.tk.update()
            self.tk.update_idletasks()
            if self.stop == True:
                self.tk.destroy()
                break

# Instantiate the class and run the main method
gt = Tank()
gt.main()
