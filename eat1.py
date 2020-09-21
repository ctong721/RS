import pyxel
import random as r

class World():
    point = []
    
    def __init__(self,w,h,s,e):
        self.w = w
        self.h = h
        self.point = [[0 for i in range(h)] for j in range(w)]
        for i in range(w):
            for j in range(h):
                self.point[i][j]=r.randrange(10,12)
        for i in range(s):
            self.point[r.randrange(0,160)][r.randrange(0,120)]=11
        for i in range(e):
            self.point[r.randrange(0,160)][r.randrange(0,120)]=9
        self.point[50][50]=11 #11绿色陆地 10沙堆 9吃的

class User:
    def __init__(self,name,world,x,y,color,zt,eat):
        self.name = name
        self.world = world
        self.x = x
        self.y = y
        self.color = color
        self.zt = zt
        self.eat = eat
    
    def move(self):
        _zt = [0,0,0,0]
        _cz = []
        _zx = -1

        if (self.x+1)<self.world.w:
            _zt[0] = self.world.point[self.x+1][self.y]
        else:
            _zt[0] = 0
        if (self.y+1)<self.world.h:
            _zt[1] = self.world.point[self.x][self.y+1]
        else:
            _zt[1] = 0
        if (self.x-1)>=0:
            _zt[2] = self.world.point[self.x-1][self.y]
        else:
            _zt[2] = 0
        if (self.y-1)>=0:
            _zt[3] = self.world.point[self.x][self.y-1]
        else:
            _zt[3] = 0
        
        for j in range(4):
            if _zt[j] in [11,9]:
                _cz.append(j)
        if len(_cz)!=0:
            _zx = _cz[r.randrange(0,len(_cz))]
        if _zx>=0:
            if _zx==0:
                self.x = self.x+1
                if self.x>=self.world.w:
                    self.x = self.world.w
            elif _zx==1:
                self.y = self.y+1
                if self.y>=self.world.h:
                    self.y = self.world.h
            elif _zx==2:
                self.x = self.x-1
                if self.x<=0:
                    self.x = 0
            elif _zx==3:
                self.y = self.y-1
                if self.y<=0:
                    self.y = 0

        if self.world.point[self.x][self.y]==9:
            self.eat = self.eat+1
            self.world.point[self.x][self.y] = 11

class App():
    def __init__(self, world, us, s, c):
        self.world = world
        self.us = us
        self.point = self.world.point
        pyxel.init(self.world.w, self.world.h, scale=s, caption=c)
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.frame_count%2==0:
            for i in range(len(self.us)):
                self.us[i].move()
    
    def draw(self):
        pyxel.cls(0)
        for i in range(self.world.w):
            for j in range(self.world.h):
                pyxel.rect(i,j,1,1,self.point[i][j])
        for i in range(len(self.us)):
            if self.us[i].zt==1:
                pyxel.rect(self.us[i].x, self.us[i].y, 1, 1, self.us[i].color)


if __name__ == '__main__':
    w = 160
    h = 120
    w1 = World(w,h,30000,100)
    us = []
    for i in range(500):
        us.append(User('u'+str(i), w1, 80, 60, r.randrange(0,9), 1, 0))
    App(w1,us,5,"")

