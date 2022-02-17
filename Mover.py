import math
import numpy as np
from SetApp import *

        
class Vec2d:
    def __init__(self,x=0,y=0): self.x = x; self.y = y
    def copy(self): return Vec2d(self.x, self.y)
    def set(self,x,y): self.x = x; self.y = y; return self
    def add(self,n): self.x += n.x; self.y += n.y; return self
    def sub(self,n): self.x -= n.x; self.y -= n.y; return self
    def mlt(self,n): self.x *= n;   self.y *= n  ; return self 
    def mag(self): return math.sqrt(self.x**2 + self.y**2)
    def norm(self): return self.copy().mlt(1/self.mag())
    def get_angle (self): return math.atan2(self.y, self.x)*180/math.pi
    def set_angle (self, angle): 
        self.x = np.cos(np.radians(angle))
        self.y = np.sin(np.radians(angle))
        return self
    def tonp (self): return np.array([self.x,self.y])
    

class Mover:
    def __init__(self):
        self.lpos = Vec2d(0,0)
        self.vpos = Vec2d(0,0)
        self.apos = Vec2d(0,0)
        
        self.langle = 0
        self.vangle = 0
        self.aangle = 0
        self.normalVec = Vec2d(1,0)
        
        self.airDrag = 0
        self.friction = 0
        self.mass = 1
        
        self.fixture = 0
        self.fixtureOrigin = np.array([[-5,5],[5,5],[5,-5],[-5,-5]])
        self.set_fixture_angle(self.langle)
        
    def update(self):
        self.vpos.add(self.apos)
        self.lpos.add(self.vpos)
        self.apos.mlt(0)
        
        self.vangle+=self.aangle
        self.langle+=self.vangle
        self.aangle=0
        
        self.vpos.mlt(1-self.airDrag)
        if self.vpos.mag() >= self.friction:
            self.vpos.sub(self.vpos.norm().mlt(self.friction))
        else: self.vpos.mlt(0)
        
        self.set_fixture_angle(self.langle)
        
        self.update_edge()
        

    def set_fixture_angle (self, angle):
        x = self.fixtureOrigin[:,0]
        y = self.fixtureOrigin[:,1]
        newX = np.cos(np.radians(angle))*x - np.sin(np.radians(angle))*y
        newY = np.sin(np.radians(angle))*x + np.cos(np.radians(angle))*y
        self.fixture = np.vstack((newX,newY)).transpose()
        
        
    def update_edge (self):
        flag = 0
        if self.lpos.x > AppData.screen_w: self.lpos.x = AppData.screen_w-1; flag='x'
        if self.lpos.x < 0:                self.lpos.x = 1; flag='x'
        
        if self.lpos.y > AppData.screen_h: self.lpos.y = AppData.screen_h-1; flag='y'
        if self.lpos.y < 0:                self.lpos.y = 1; flag='y'
        
        if flag=='x': self.vpos.x = -self.vpos.x
        if flag=='y': self.vpos.y = -self.vpos.y
        
def collide_check (obj1, obj2):
    # OBB 충돌체크
    
    # 물체의 x길이를 잽니다.
    o1Xrange = obj1.fixture[:,0].max() - obj1.fixture[:,0].min()
    o2Xrange = obj2.fixture[:,0].max() - obj2.fixture[:,0].min()
    # 물체의 y길이를 잽니다.
    o1Yrange = obj1.fixture[:,1].max() - obj1.fixture[:,1].min()
    o2Yrange = obj2.fixture[:,1].max() - obj2.fixture[:,1].min()
    
    # 물체사이의 길이를 잽니다.
    o12range = obj2.lpos.copy().sub(obj1.lpos)
    
    if o1Xrange/2 + o2Xrange/2 > abs(o12range.x): 
        if o1Yrange/2 + o2Yrange/2 > abs(o12range.y): 
            return True
    return False

def update_collide(obj1, obj2):
    # elastic collision in sphere
    ek1 = obj1.mass*obj1.vpos.mag()**2/2
    ek2 = obj2.mass*obj2.vpos.mag()**2/2
    
    v1x = ((obj1.mass - obj2.mass)*obj1.vpos.x + 2*obj2.mass*obj2.vpos.x)/(obj1.mass+obj2.mass)
    v1y = ((obj1.mass - obj2.mass)*obj1.vpos.y + 2*obj2.mass*obj2.vpos.y)/(obj1.mass+obj2.mass)
    v2x = ((obj2.mass - obj1.mass)*obj2.vpos.x + 2*obj1.mass*obj1.vpos.x)/(obj2.mass+obj1.mass)
    v2y = ((obj2.mass - obj1.mass)*obj2.vpos.y + 2*obj1.mass*obj1.vpos.y)/(obj2.mass+obj1.mass)
    obj1.vpos.set(v1x, v1y)
    obj2.vpos.set(v2x, v2y)