class Slider(object):
    
    def __init__(self, x, y, w, h, low, high, default):
        # (x, y) are the cordinates of the top left of the slider
        # (w, h) are the width and height of the slider extending to the right and downward
        # (low, high) the lowest and highest numbers on the slider
        # default value: starting value of the slider
        
        if default < low or default > high:
            raise Exception("Default value outside given interval")
        
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.low = low
        self.high = high
        self.value = default
            
        self.drawSlider(self.y+self.h*0.9-(((self.h*0.8)*(self.value-self.low))/(self.high-self.low)))
    
    def get_Value(self):
        if mousePressed:
            if dist(self.x+self.w*0.5, self.y+self.h*0.9-(((self.h*0.8)*(self.value-self.low))/(self.high-self.low)), mouseX, mouseY) < self.w*0.3:
                if (mouseY > self.y) and (mouseY < self.y+self.h):
                    
                    self.value = (((self.y+self.h*0.9)-mouseY)/(self.h*0.8)) * (self.high-self.low) + self.low
                    if (self.value > self.high):
                        self.value = self.high
                    elif (self.value < self.low):
                        self.value = self.low
                    self.drawSlider(mouseY)
                else:
                    self.drawSlider(self.y+self.h*0.9-(((self.h*0.8)*(self.value-self.low))/(self.high-self.low)))
            else:
                self.drawSlider(self.y+self.h*0.9-(((self.h*0.8)*(self.value-self.low))/(self.high-self.low)))
        else:
            self.drawSlider(self.y+self.h*0.9-(((self.h*0.8)*(self.value-self.low))/(self.high-self.low)))
        return self.value
    
    def set_Value(self,newValue):
        if newValue < self.low or newValue > self.high:
            raise Exception("newValue out of given range")
        self.value = newValue
        self.drawSlider(self.y+self.h*0.9-(((self.h*0.8)*(self.value-self.low))/(self.high-self.low)))
    
    def drawSlider(self, sliderY):
        rectMode(CORNER)
        fill(255)
        strokeWeight(1)
        stroke(0)
        rect(self.x,self.y,self.w,self.h)
        strokeWeight(4)
        stroke(180)
        line(self.x+self.w*0.5,self.y+self.h*0.1,self.x+self.w*0.5,self.y+(self.h*(0.9)))
        strokeWeight(1)
        stroke(0)
        rectMode(CENTER)
        fill(0)
        rectY = sliderY
        if (rectY < self.y+self.h*0.1):
            rectY = self.y+self.h*0.1
        elif (rectY > self.y+(self.h*(0.9))):
            rectY = self.y+(self.h*(0.9))
        rect(self.x+self.w*0.5, rectY,self.w*0.3,self.h*0.05)
        textAlign(CENTER,TOP)
        text(self.high, self.x+self.w*0.5,self.y+self.h*0.01)
        textAlign(CENTER,TOP)
        text(self.low, self.x+self.w*0.5,self.y+(self.h*(0.92)))
        
class MovablePoint(object):
    
    def __init__(self, x, y, r, c):
        # (x, y) are the cordinates of the point
        # r is the radius or the stroke of the point drawing
        # c is how close the users mouse has to be to move the point
        
        self.x = x
        self. y = y
        self.r = r
        self.c = c
        
        self.drawPoint()
        
    def getPosition(self):
        #returns position in array with format [x,y]
        if mousePressed:
            if dist(self.x,self.y,mouseX,mouseY) <= self.c:
                self.x = mouseX
                self.y = mouseY
        self.drawPoint()
        return([self.x,self.y])
                
    def setPosition(self, x , y):
        self.x = x
        self.y = y
        
    def drawPoint(self):
        strokeWeight(self.r)
        stroke(0)
        point(self.x,self.y)
        

value = 0
new_value = 0
slider = None
new_slider = None
point_one = None

def setup():
    global slider, new_slider, point_one
    size(500,500)
    background(255)
    new_slider = Slider(300,100,50,200,10,20,15)
    point_one = MovablePoint(150,150,8,12)
    
def draw():
    global slider, value, new_slider, new_value, point_one
    background(255)
    new_value = new_slider.get_Value()
    point_cord = point_one.getPosition()
    
