import math
import numpy as np

class Vec2d:
    def __init__(self,x,y): self.x = x; self.y = y
    def copy(self): return Vec2d(self.x, self.y)
    def add(self,n): self.x += n.x; self.y += n.y; return self
    def sub(self,n): self.x -= n.x; self.y -= n.y; return self
    def mlt(self,n): self.x *= n;   self.y *= n  ; return self 
    def mag(self): return math.sqrt(self.x**2 + self.y**2)
    def norm(self): self.copy().mlt(1/self.mag())
    def get_angle (self): return math.atan2(self.y, self.x)*180/math.pi
    def tolist (self): return [self.x,self.y]