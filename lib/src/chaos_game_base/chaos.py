# @title imports
import matplotlib.pyplot as plt
import numpy as np
from random import choices

#  @title Helper Functions

# create index population by given probability distribution
def create_population(probs, count=1):
  population = np.arange(len(probs))
  return choices(population, probs, k=count)

# affine transformation matrix mult
def matrix_mult(op, p):
    x = op[0][0]*p[0] + op[0][1]*p[1] + op[0][2]*p[2]
    y = op[1][0]*p[0] + op[1][1]*p[1] + op[1][2]*p[2]
    return [x,y,1]

def chaos_game(n, hutch, probs, init=[0,0]):
    x_out = []
    y_out = []
    point = [*init,1]
    op_out = create_population(probs, n)
    for p in op_out:
      next = matrix_mult(hutch[p], point)
      x_out.append(next[0])
      y_out.append(next[1])
      point = next

    return x_out, y_out, op_out

# @title Base classes
class ChaosGameOutput:

  def __init__(self, x_out, y_out, op_out, n):
    self.x_out = x_out
    self.y_out = y_out
    self.op_out = op_out
    self.n = n
    self.c = 'tab:green'
    self.c_out = []

  def color(self, colors):
    if type(colors) == str:
      self.c = colors
    elif type(colors) == list:
      self.c_out = colors
    elif callable(colors):
      self.c_out = colors(self)
    else:
      print(f"invalid arg {colors} of type {type(colors)} for the function color")

  def plot(self, size=(8,8)):
    colors = self.c_out if len(self.c_out) == len(self.x_out) else self.c
    plt.figure(figsize=(size[0],size[1]))
    plt.scatter(self.x_out, self.y_out, marker='.', s=0.5, color=colors)
    plt.show()

class ChaosGame:

  def __init__(self, transformations, probabilities):
    self.transformations = transformations
    self.probabilities = probabilities

  def play(self, n):
    x_out, y_out, op_out = chaos_game(n, self.transformations, self.probabilities)
    return ChaosGameOutput(x_out, y_out, op_out, n)

# @title class DefaultFernChaosGame
class DefaultFernChaosGame(ChaosGame):

  def __init__(self):
    fern_transformations, fern_probs = DefaultFernChaosGame.get()
    ChaosGame.__init__(self, fern_transformations, fern_probs)

  def get():
    # Transformations
    STEM = [[0,0,0],
        [0,0.16,0]]

    GROW = [[0.85,0.04,0],
          [-0.04,0.85,1.6]]

    LEFT = [[0.2,-0.26,0],
          [0.23,0.22,1.6]]

    RIGHT = [[-0.15,0.28,0],
          [0.26,0.24,0.44]]

    fern_transformations = [STEM, GROW, LEFT, RIGHT]
    fern_probs = [0.01, 0.85, 0.07, 0.07]

    return fern_transformations, fern_probs