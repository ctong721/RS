import pyxel
import random as r

w = 160
h = 120
pyxel.init(w, h, scale=6)
user = [{'name':'u1','x':50,'y':50,'zt':1,'color':8,'eat':0},
{'name':'u2','x':55,'y':50,'zt':1,'color':4,'eat':0},
{'name':'u3','x':50,'y':55,'zt':1,'color':5,'eat':0}]

def f1(c, v):
    point = []
    x0 = r.random()*w
    y0 = r.random()*h
    for i in range(c):
        lx = r.randrange(-v,v+1)
        ly = r.randrange(-v,v+1)
        point.append({'x':x0, 'y':y0, 'color':r.randrange(10,15)})
        x0 = x0+lx
        y0 = y0+ly
        if x0<0:
            x0 = r.random()*w
        if y0<0:
            y0 = r.random()*h
    return point

def f2(w,h,s,e):
    point = [[0 for i in range(h)] for j in range(w)]
    for i in range(w):
        for j in range(h):
            point[i][j]=r.randrange(10,12)
    for i in range(s):
        point[r.randrange(0,160)][r.randrange(0,120)]=11
    for i in range(e):
        point[r.randrange(0,160)][r.randrange(0,120)]=9
    point[50][50]=11 #11绿色陆地 10沙堆 9吃的
    return point


def move():
    for i in range(len(user)):
        if p1[user[i]['x']+1][user[i]['y']]==11:
            user[i]['x']=user[i]['x']+1
        elif p1[user[i]['x']][user[i]['y']+1]==11:
            user[i]['y']=user[i]['y']+1
        
def move1():
    for i in range(len(user)):
        zt = [0,0,0,0]
        cz = []
        zx = -1
        zt[0]=p1[user[i]['x']+1][user[i]['y']]
        zt[1]=p1[user[i]['x']][user[i]['y']+1]
        zt[2]=p1[user[i]['x']-1][user[i]['y']]
        zt[3]=p1[user[i]['x']][user[i]['y']-1]
        for j in range(4):
            if zt[j] in [11,9]:
                cz.append(j)
        if len(cz)!=0:
            zx = cz[r.randrange(0,len(cz))]
        if zx>=0:
            if zx==0:
                user[i]['x']=user[i]['x']+1
            elif zx==1:
                user[i]['y']=user[i]['y']+1
            elif zx==2:
                user[i]['x']=user[i]['x']-1
            elif zx==3:
                user[i]['y']=user[i]['y']-1
        
        if p1[user[i]['x']][user[i]['y']]==9:
            user[i]['eat'] = user[i]['eat']+1
            p1[user[i]['x']][user[i]['y']]=11
        
        for j in range(len(user)):
            if j!=i:
                if user[i]['x']==user[j]['x']:
                    if user[i]['y']==user[j]['y']:
                        if user[i]['eat']>user[j]['eat']:
                            user[j]['zt']=0
                        elif user[i]['eat']<user[j]['eat']:
                            user[i]['zt']=0

##################################
def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    if pyxel.frame_count%2==0:
        move1()

def draw():
    pyxel.cls(0)
    for i in range(w):
        for j in range(h):
            pyxel.rect(i,j,1,1,p1[i][j])
    pyxel.text(0,0,str(pyxel.frame_count),8)
    pyxel.text(20,0,str(user[0]['eat']),8)
    pyxel.text(30,0,str(user[1]['eat']),4)
    pyxel.text(40,0,str(user[2]['eat']),5)
    for i in range(len(user)):
        if user[i]['zt']==1:
            pyxel.rect(user[i]['x'],user[i]['y'],1,1,user[i]['color'])

##################################
p1 = f2(w,h,30000,100)
pyxel.run(update, draw)
