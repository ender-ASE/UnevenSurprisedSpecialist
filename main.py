#Class for a Boat.
class Boat:

  isBoatDocked=False

  isAnchorDropped=False

  currentSpeed=0

  currentFuel=100
  
  def __init__(self,engineSizeInput,colorInput,frameSize,boatName):
    self.engine=engineSizeInput
    self.color=colorInput
    self.frame=frameSize
    self.name=boatName

  def dock(self):
    if self.isBoatDocked==False:
      self.isBoatDocked=True
      print("We should dock soon.")
    else:
      print("we are already docked")
  

  def refuel(self):
    if self.currentFuel == 100:
      print("You don't need to refuel")
    else:
      while self.currentFuel < 100:
        self.currentFuel += 1
        print("Your fuel level is "+str(self.currentFuel))  
  
  def speedUp(self,speedChange):
    self.currentSpeed += speedChange
    if self.currentFuel - speedChange/2 <= 0:
      print("WARNING - FUEL DEPLETED")
    else:
      self.currentFuel -= speedChange/2
    print("Your speed is "+str(self.currentSpeed))
    print("Your fuel level is: "+str(self.currentFuel))

  def slowDown(self,speedChange):
    self.currentSpeed -= speedChange
    print("Your speed is "+str(self.currentSpeed))

  def anchorDrop(self):
    if self.isAnchorDropped==False:
      self.isAnchorDropped=True
      print("Drop Anchor")
    else:
      print("Anchor Already Dropped")

print("Welcome To Mr. Russ' Boat Factory")
print("What size engine do you want?")
userEngineInput=input()
print("What color boat do you want?")
userColorInput=input()
print("What frame size do you want?")
userFrameSizeInput=input()
print("What do you want to name your boat?")
userBoatNameInput=input()

JacksonsBoat=Boat(userEngineInput,userColorInput,userFrameSizeInput,userBoatNameInput)

JacksonsBoat.refuel()