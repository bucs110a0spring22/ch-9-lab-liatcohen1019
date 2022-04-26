from Rectangle import Rectangle 
class Surface: 
  def __init__(self, filename, x, y, h, w):
    #saves the variables as parameter and makes them insatnce variables 
    self.image = filename 

    self.rect = Rectangle(x, y, h, w)
    #returns the rectangle object 
  def getRect(self):
      return self.rect