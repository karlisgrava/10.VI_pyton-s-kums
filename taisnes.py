import math 
#koeficentu noteiksana taisnes vienadojumam
def l_koef(x1,y1,x2,y2):
        k=(y1-y2)/(x1-x2)
        b=(y1-k*x1)
        koef=[]
        koef.append(k)
        koef.append(b)
        return koef
def p_koord (x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    x3=x1+2*dx
    y3=x1+2*dy
    p=[]
    p.append(x3)
    p.append(y3)
    return p
xa=float(input("ievadi xa: "))
ya=float(input("ievadi ya: "))
xb=float(input("ievadi xb: "))
yb=float(input("ievadi yb: "))
xc=float(input("ievadi xc: "))
yc=float(input("ievadi yc: "))
#parbaude
#seit vajag
xo=float(input("ievadi xo: "))
yo=float(input("ievadi yo: "))
#a_O xa ya xo yo
#y=kx+b
# xa ya xb yb xc yc xo yo
a1=[]
b1=[]
c1=[]
print(p_koord (xa,ya,xo,yo)) #a1 p_koord
print(p_koord (xb,yb,xo,yo)) #b1 p_koord
print(p_koord (xc,yc,xo,yo)) #c1 p_koord