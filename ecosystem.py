import random 

class River:
  def __init__(self,size,numFish,numBear):
    self.size = size
    self.river = [["🟦 " for x in range(size)] for y in range(size)]
    self.numBear = numBear
    self.numFish = numFish
    self.animals = []
    self.newanimals = []
    self.population = 0
    self.maxPop = size * size
    self.__inital_population()


  def __inital_population(self):
    for ani in range(self.numFish):
      self.placeBaby(Fish)
    for ani in range(self.numBear):
      self.placeBaby(Bear)

  
  def placeBaby(self,ani):
    x = random.randint(0, self.size-1)
    y = random.randint(0, self.size-1)
    while self.river[y][x] != "🟦 ":
      x = random.randint(0, self.size-1)
      y = random.randint(0, self.size-1)
    baby = ani(x,y)
    self.river[y][x] = baby
    self.animals.append(baby)
    self.population += 1



  def animalDeath(self,ani):
    self.river[ani.y][ani.x] = "🟦 "
    self.animals.remove(ani) 
    self.population -= 1 

  def redrawCells(self,ani,dx,dy):
    self.river[ani.y+dy][ani.x+dx] = ani
    self.river[ani.y][ani.x] = "🟦 "
    ani.y += dy
    ani.x += dx 

  def new_day(self):
    for animal in self.animals:
      animal.bredToday = False
    for animal in self.animals:
      animal.move(self)
    for animal in self.animals:
      if type(animal) == Bear:
        if animal.eatenToday == False:
          animal.starve(self)
        animal.eatenToday = False
    for animal in self.newanimals:
      if self.population < self.maxPop: 
        self.placeBaby(animal)
      else: # this doesnt seem to get called idk why tho :(
        print("to many animals")
        return True
    self.newanimals = []
    return False
    

  def __str__(self):
    riverMap = ""
    for row in self.river:
      for item in row:
        riverMap += str(item)
      riverMap += "\n"
    return riverMap

  def __getitem__(self, i):
    return self.river[i]

class Animal:
  def __init__(self, x, y):
    self.x = x
    self.y = y 
    self.bredToday = False

  def death(self,river):
    river.animalDeath(self)
    
  def move(self,r):
    dx = random.randint(-1,1)
    dy = random.randint(-1,1)

    while not(0 <= self.y + dy < r.size) or not(0 <= self.x + dx < r.size):
      dx = random.randint(-1,1)
      dy = random.randint(-1,1)

    if r.river[self.y + dy][self.x + dx] == "🟦 ":
      r.redrawCells(self,dx,dy)
    else:
      self.collison(r.river[self.y+dy][self.x + dx],r)

  def collison(self, otherAni, r):

    if type(self) == type(otherAni): #same animal meaning they kiss
      if type(self) == Bear:
        if self.bredToday == False and otherAni.bredToday == False:
          r.newanimals.append(Bear)
          self.bredToday = True
          otherAni.bredToday = True
      else:
        if self.bredToday == False and otherAni.bredToday == False:
          r.newanimals.append(Fish)
          self.bredToday = True
          otherAni.bredToday = True

    else: #diff animals meaning they get nasty
      if type(self) == Bear: #bear is self
        self.consume()
        otherAni.death(r)
        r[otherAni.y][otherAni.x] = self
        self.y = otherAni.y
        self.x = otherAni.x     

      elif type(self) == Fish:#fish is self
        otherAni.consume()
        self.death(r)

 
class Bear(Animal):
  def __init__(self, x, y):
    super().__init__(x,y)
    self.maxLives = 9
    self.lives = 7
    self.eatenToday = False

  def starve(self,r):
    self.lives -= 1
    if self.lives <= 0:
      self.death(r)
  
  def consume(self):
    if self.eatenToday == False:
      self.eatenToday = True
      if self.lives > self.maxLives:
        self.lives += 1

  def __str__(self):
    return "🐻 "



class Fish(Animal): 
  def __init__(self, x, y):
    super().__init__(x,y)

  def __str__(self):
    return "🐟 "


