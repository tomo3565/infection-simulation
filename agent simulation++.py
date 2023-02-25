from tkinter import *
from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import time, random



tk = Tk()
canvas = Canvas(tk, width=2000, height=1000)
canvas.pack()

canvas.delete("all")

def draw_square_at(x, y, w, h):
    bottom_x = x + w   # 家のbottom x
    bottom_y = y + h   # 家のbottom y

    # 四角形で家を描く(左上と右下の座標を指定する。)
    canvas.create_rectangle(x, y, bottom_x, bottom_y)

print("COCOAの普及率(%)：")
haveacocoa=int(input())
print("接触後の外出確率の減少値(%)：")
cocoa_outing=int(input())

x0 = 10
y0=500
W = 38
H = 28
PAD=8

for y in range(10):
    for x in range(33):
        draw_square_at(x0, y0, W, H)
        x0 += W + PAD
    y0= y0 + H + PAD    
    x0=10
for x in range(3):
        draw_square_at(x0, y0, W, H)
        x0 += W + PAD

        
x0 = 10
y0=10
W = 350
H = 230
PAD=20
for y in range(2):
    for x in range(3):
        draw_square_at(x0, y0, W, H)
        x0 += W + PAD
    y0= y0 + H + PAD    
    x0=10

draw_square_at(1120, 100, 390, 270)

def having_cocoa(haveacocoa):
    if random.random()*100 <= haveacocoa:
        return 1
    else:
        return 0
        

@dataclass
class Agent:
    identity: int #0:会社員 1:主婦/主婦 2:学生
    home_number:int #それぞれの家族に番号を与える
    counter: int  # 潜伏, 発症 から何日経ったか
    status: str  #"S":健康/ "E":潜伏/ "I":発症/ "R" :回復/ "D":死亡
    cocoa: int #1:持っている  0:持っていない
    cocoa_switch: int #1:COCOAが反応  0:COCOA反応なし
    cocoa_counter: int #COCOAが反応してから、何日経ったか。
    outing_rate: int  #外出率
    goto_time: int #外出時刻　10分単位
    outing_time: int #外出時間　10分単位
    goto: int #外出先
    oid:int
    
Home=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
      [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
      [],[],[]]


count=0
for home_number in Home:
    for x in range(3):
        if x == 0:
            home_number.append(Agent(x,
                                     count,
                                     3,
                                     "S",
                                     having_cocoa(haveacocoa),
                                     0,
                                     0,
                                     random.choice([99,100]),
                                     int(np.random.normal(51, 9, None)),
                                     random.randint(36, 48),
                                     random.choice([0,1])
                                    ,0))
        elif x == 1:
            home_number.append(Agent(x,
                                     count,
                                     3,
                                     "S",
                                     having_cocoa(haveacocoa),
                                     0,
                                     0,
                                     random.randint(50, 100),
                                     int(np.random.normal(63, 9, None)),
                                     random.randint(3, 6),
                                     random.choice([0,1]),0))
        elif x == 2:
            home_number.append(Agent(x,
                                     count,
                                     3,
                                     "S",
                                     having_cocoa(haveacocoa),
                                     0,
                                     0,
                                     random.choice([99,100]),
                                     int(np.random.normal(51, 9, None)),
                                     random.randint(30, 36),
                                     random.choice([0,1]),0))
    count = count + 1

Home[2][0]=Agent(0,2,3,"E",having_cocoa(haveacocoa),0,0,random.choice([99,100]),int(np.random.normal(51, 9, None)),random.randint(36, 48),random.choice([0,1]),0)
Home[3][0]=Agent(0,3,3,"E",having_cocoa(haveacocoa),0,0,random.choice([99,100]),int(np.random.normal(51, 9, None)),random.randint(36, 48),random.choice([0,1]),0)
Home[11][0]=Agent(0,11,3,"E",having_cocoa(haveacocoa),0,0,random.choice([99,100]),int(np.random.normal(51, 9, None)),random.randint(36, 48),random.choice([0,1]),0)
Home[5][1]=Agent(1,5,3,"E",having_cocoa(haveacocoa),0,0,random.randint(50, 100),int(np.random.normal(63, 9, None)),random.randint(3, 6),random.choice([0,1]),0)
Home[7][1]=Agent(1,7,3,"E",having_cocoa(haveacocoa),0,0,random.randint(50, 100),int(np.random.normal(63, 9, None)),random.randint(3, 6),random.choice([0,1]),0)
Home[20][1]=Agent(1,20,3,"E",having_cocoa(haveacocoa),0,0,random.randint(50, 100),int(np.random.normal(63, 9, None)),random.randint(3, 6),random.choice([0,1]),0)
Home[18][2]=Agent(2,18,3,"E",having_cocoa(haveacocoa),0,0,random.choice([99,100]),int(np.random.normal(51, 9, None)),random.randint(30, 36),random.choice([0,1]),0)
Home[17][2]=Agent(2,17,3,"E",having_cocoa(haveacocoa),0,0,random.choice([99,100]),int(np.random.normal(51, 9, None)),random.randint(30, 36),random.choice([0,1]),0)
Home[13][2]=Agent(2,13,3,"E",having_cocoa(haveacocoa),0,0,random.choice([99,100]),int(np.random.normal(51, 9, None)),random.randint(30, 36),random.choice([0,1]),0)

    
School=[[],[]]

Shop=[[],[]]

Company=[[],[]]



Hospital=[]

Tomb=[]


x0 = 10
y0=500
W = 38
H = 28
PAD=8
r=10
pp=0
for home_number in Home:
            pp = pp +1
            for agent in home_number:
                xx=random.randint(x0+10,x0+W-10)
                yy=random.randint(y0+10,y0+H-10)
                if agent.status=="E":
                    object_id=canvas.create_oval(xx-r/2, yy-r/2, xx+r/2, yy+r/2, fill="yellow")
                else:
                    object_id=canvas.create_oval(xx-r/2, yy-r/2, xx+r/2, yy+r/2, fill="blue")
                agent.oid=object_id
            x0 += W + PAD
            if pp == 33:
                x0 = 10
                y0 = y0 + H + PAD
                pp=0


 

def C_place(place):#場所ごとの感染判定
    for a in place:
        if a.status == "I":
            for b in place:
                if b.status == "S":
                    if random.random()*10 <= 9:  #接触する確率
                        if b.cocoa == 1: 
                            b.cocoa_switch = 1 #もし接触したら、COCOAが反応
                        if random.random() <= 0.0002:
                            b.status = "E" #接触した際、感染する確率
                            canvas.itemconfigure(b.oid, fill="yellow")
        elif a.status == "E":
            if a.counter == 4:
                for b in place:
                    if b.status == "S":
                        if random.random()*10 <= 9:  #接触する確率
                            if b.cocoa == 1: 
                                b.cocoa_switch = 1 #もし接触したら、COCOAが反応
                            if random.random() <= 0.0002:
                                b.status = "E" #接触した際、感染する確率
                                canvas.itemconfigure(b.oid, fill="yellow")
                

def C():#全ての場所で感染判定を行う
    for house in Home:
        C_place(house)
    for company_number in Company:
        C_place(company_number)
    for shop_number in Shop:
        C_place(shop_number)
    for school_number in School:
        C_place(school_number)
        
    
                            
def Cocoa_place(place): #場所ごとのCoCCa反応判定
    for x in place:
        if x.cocoa == 1 and x.cocoa_switch == 1:
            x.outing_rate = x.outing_rate * (100 - cocoa_outing)/100

def Cocoa(): #全ての場所でCocoa反応判定を行う
    for house in Home:
        Cocoa_place(house)
    for company_number in Company:
        Cocoa_place(company_number)
    for shop_number in Shop:
        Cocoa_place(shop_number)
    for school_number in School:
        Cocoa_place(school_number)


    

def T1(home): #状態の移り変わり(潜伏→感染)を定義する→変化に応じて、エージェントの場所(病院)を移す。
    global infected_count
    for home_number in home:
        for agent in home_number:
            if agent.status == "E" or agent.status == "I":
                agent.counter = agent.counter + 1
                if agent.counter >= 5:
                    agent.status = "I"
                    canvas.itemconfigure(agent.oid, fill="red")
                    if random.random()*100 <= agent.counter*10:
                        agent.counter = 0
                        home_number.remove(agent)
                        Hospital.append(agent)
                        h=random.randint(1120+5,1120+390-5)
                        i=random.randint(100+5,100+270-5)
                        canvas.coords(agent.oid,h-10/2, i-10/2, h+10/2, i+10/2)
                    
                                        
                    
                
def T2(hospital):#状態の移り変わり(感染→回復/死亡)を定義する→変化に応じて、エージェントの場所(墓/家)を移す。
    for agent in hospital:
        if agent.status == "I":
            agent.counter = agent.counter + 1
            if agent. counter == 14:
                agent.counter = 0
                if random.random()*100 > 5: #95%で回復 
                    agent.status = "R"
                    Hospital.remove(agent)
                    Home[agent.home_number].append(agent)
                    d=int(agent.home_number/33)
                    c=agent.home_number % 33
                    e=random.randint(46*c+10+5, 46*c+10+38-5)
                    f=random.randint(500+36*d+5,500+36*d+36-5)
                    canvas.coords(agent.oid,e-10/2, f-10/2, e+10/2, f+10/2)
                    canvas.itemconfigure(agent.oid, fill="green")
                else: #5%で死亡
                    agent.status = "D"
                    canvas.itemconfigure(agent.oid, fill="black")


def T3 (home): #Cocoaによる、外出率の移り変わりを定義する。
    for home_number in home:
        for agent in home_number:
            if agent.cocoa_switch == 1:
                agent.cocoa_counter = agent.cocoa_counter + 1
            if agent.cocoa_counter >= 14: #COCOA反応から、2週間経過すると、自粛をやめる
                agent.cocoa_switch = 0
                agent.cocoa_counter = 0
                if agent.identity==0:
                    agent.outing_rate = random.randint(99,100)
                elif agent.identity==1:
                    agent.outing_rate = random.randint(50,100)
                elif agent.identity==2:
                    agent.outing_rate = random.randint(99,100)
def T():
    T1(Home)
    T2(Hospital)
    T3(Home)
            

                    

def Outing(time): #外出するかしないか
    for home_number in Home:
        for agent in home_number:
            if agent.outing_rate > random.random()*100:
                if agent.identity == 0:#会社員の場合
                    if time == agent.goto_time:
                        home_number.remove(agent)
                        Company[agent.goto].append(agent)
                        if agent.goto == 0:
                            a=random.randint(10+5,10+350-5)
                            b=random.randint(10+5,10+230-5)
                            canvas.coords(agent.oid,a-10/2, b-10/2, a+10/2, b+10/2)
                        else:
                            a=random.randint(10+5,10+350-5)
                            b=random.randint(10+230+20+5,10+230+20+230-5)
                            canvas.coords(agent.oid,a-10/2, b-10/2, a+10/2, b+10/2)
                        
                if agent.identity == 1:#主婦/主夫の場合
                    if time == agent.goto_time:
                        home_number.remove(agent)
                        Shop[agent.goto].append(agent)
                        if agent.goto == 0:
                            a=random.randint(10+350+20+5,10+350+20+350-5)
                            b=random.randint(10,10+230)
                            canvas.coords(agent.oid,a-10/2, b-10/2, a+10/2, b+10/2)
                        else:
                            a=random.randint(10+350+20+5,10+350+20+350-5)
                            b=random.randint(10+230+20+5,10+230+20+230-5)
                            canvas.coords(agent.oid,a-10/2, b-10/2, a+10/2, b+10/2)
                if agent.identity == 2:#学生の場合
                    if time == agent.goto_time:
                        home_number.remove(agent)
                        School[agent.goto].append(agent)
                        if agent.goto == 0:
                            a=random.randint(10+350+20+350+20+5,10+350+20+350+20+350-5)
                            b=random.randint(10+5,10+230-5)
                            canvas.coords(agent.oid,a-10/2, b-10/2, a+10/2, b+10/2)
                        else:
                            a=random.randint(10+350+20+350+20+5,10+350+20+350+20+350-5)
                            b=random.randint(10+230+20+5,10+230+20+230-5)
                            canvas.coords(agent.oid,a-10/2, b-10/2, a+10/2, b+10/2)
            
def Back_place(place, time): #各外出先から帰宅させる
    for place_number in place:
        for agent in place_number:
            if time >= agent.goto_time + agent.outing_time:
                place_number.remove(agent)
                Home[agent.home_number].append(agent)
                d=int(agent.home_number/33)
                c=agent.home_number % 33
                e=random.randint(46*c+10+5, 46*c+10+38-5)
                f=random.randint(500+36*d+5,500+36*d+28-5)
                canvas.coords(agent.oid,e-10/2, f-10/2, e+10/2, f+10/2)
                

def coords():
    for house in Home:
        for agent in house:
            d=int(agent.home_number/33)
            c=agent.home_number % 33
            e=random.randint(46*c+10+5, 46*c+10+38-5)
            f=random.randint(500+36*d+5,500+36*d+28-5)
            canvas.coords(agent.oid,e-10/2, f-10/2, e+10/2, f+10/2)
    for company_number in Company:
        for agent in company_number:
            if agent.goto == 0:
                    a=random.randint(10+5,10+350-5)
                    b=random.randint(10+5,10+230-5)
                    canvas.coords(agent.oid,a-10/2, b-10/2, a+10/2, b+10/2)
            else:
                    a=random.randint(10+5,10+350-5)
                    b=random.randint(10+230+20+5,10+230+20+230-5)
                    canvas.coords(agent.oid,a-10/2, b-10/2, a+10/2, b+10/2)
    for shop_number in Shop:
        for agent in shop_number:
            if agent.goto == 0:
                a=random.randint(10+350+20+5,10+350+20+350-5)
                b=random.randint(10+5,10+230-5)
                canvas.coords(agent.oid,a-10/2, b-10/2, a+10/2, b+10/2)
            else:
                a=random.randint(10+350+20+5,10+350+20+350-5)
                b=random.randint(10+230+20+5,10+230+20+230-5)
                canvas.coords(agent.oid,a-10/2, b-10/2, a+10/2, b+10/2)

    for school_number in School:
        for agent in school_number:
            if agent.goto == 0:
                a=random.randint(10+350+20+350+20+5,10+350+20+350+20+350-5)
                b=random.randint(10+5,10+230-5)
                canvas.coords(agent.oid,a-10/2, b-10/2, a+10/2, b+10/2)
            else:
                a=random.randint(10+350+20+350+20+5,10+350+20+350+20+350-5)
                b=random.randint(10+230+20+5,10+230+20+230-5)
                canvas.coords(agent.oid,a-10/2, b-10/2, a+10/2, b+10/2)


def Back(time):
    Back_place(School, time)
    Back_place(Shop, time)
    Back_place(Company, time)

          
x0 = 10
y0=500
W = 38
H = 28
PAD=8
r=10
pp=0



date=0
time=0
def main_loop():
            global date
            global time
            time=time+1
            infected_number = 0
            coords()
            C()
            Cocoa()
            Outing(time)
            Back(time)
            tk.after(200, main_loop)
            if time==144:
                T()
                time=0
        

tk.after(200, main_loop)
      
        
print("OK")       









