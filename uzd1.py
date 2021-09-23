import math
x1=float(input ("x1:"))
y1=float(input ("y1:"))
x2=float(input ("x2:"))
y2=float(input ("y3:"))
x3=float(input ("x3:"))
y3=float(input ("y3:"))
a12=math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
a23=math.sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3))
a31=math.sqrt((x3-x1)*(x3-x1)+(y3-y1)*(y3-y1))
print(a12,a23,a31)
if a12<(a23+a31)and a23<(a12+a31) and a31<(a12+a23):
    l=a12+a23+a31
    p2=l/2
    s=math.sqrt(p2*(p2-a12)*(p2-a23)*(p2-a31))
    e=s/l
    print("tristura efektivitate:{0:.4e}".format(e))
else:
    print("tristuri nevar izveidot")