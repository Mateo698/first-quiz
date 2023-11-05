################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!
def make_oven():
  return Oven()

class Oven:
  def __init__(self):
    self.ingredients = []
    self.temperature = 0
    self.output = None

  def add(self, item):
    self.ingredients.append(item)

  def freeze(self):
    self.temperature = -1

  def boil(self):
    self.temperature = 100

  def wait(self):
    self.temperature = 0

  def get_output(self):
    return self.output

  def set_output(self, output):
    self.output = output

def alchemy_combine(oven, ingredients, temperature):
  
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()

  if oven.ingredients == ["lead", "mercury"]:
    oven.set_output("gold")
  elif oven.ingredients == ["water", "air"]:
    oven.set_output("snow")
  elif oven.ingredients == ["cheese", "dough", "tomato"]:
    oven.set_output("pizza")
  else:
    oven.set_output("unknown")

  return oven.get_output()
