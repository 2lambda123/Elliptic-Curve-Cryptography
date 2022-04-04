import sys
import libnum

a=0
b=7
p=37

x1=6
x2=8

if (len(sys.argv)>1):
    x1=int(sys.argv[1])
if (len(sys.argv)>2):
    p=int(sys.argv[2])
if (len(sys.argv)>3):
    a=int(sys.argv[3])
if (len(sys.argv)>4):
    b=int(sys.argv[4])
if (len(sys.argv)>5):
    n=int(sys.argv[5])



print("a=",a)
print("b=",b)
print("p=",p)

print("x-point=",x1)


z=(x1**3 + a*x1 +b) % p
if (libnum.has_sqrtmod(z,{p:1} )):
    y1=next(libnum.sqrtmod(z,{p:1}))

if (y1==0):
    print("No solution for y1 on curve. Please select another x-point.")
    sys.exit()

for x2 in range(2,p-1):
    z=(x2**3 + a*x2 +b) % p
    y2=0
    if (libnum.has_sqrtmod(z,{p:1} )):
        y2=next(libnum.sqrtmod(z,{p:1}))
    
    
    if (y2!=0 and x1!=x2):
        print("P1=(%d,%d)" % (x1,y1), end=' ')
        print("\tP2=(%d,%d)" % (x2,y2), end=' ')
        
        s=(y2-y1)* libnum.invmod(x2-x1,p)
        
        x3=(s**2-x2-x1) % p
        
        y3=((s*(x2-x3)-y2)) % p
        
        print("\tP1+P2=(%d,%d)" % (x3,y3))
        if (x2>100): sys.exit()
    
    if (y2!=0 and x1==x2):
        print("P1=(%d,%d)" % (x1,y1), end=' ')
        print("\tP2=(%d,%d)" % (x2,y2), end=' ')
        
        s=((3*x1**2)+a) * libnum.invmod(2*y1,p)
        
        x2=(s**2-2*x1) % p
        
        y2=((s*(x1-x2))-y1) % p
        
        print("\tP1+P2=(%d,%d)" % (x2,y2))
        if (x2>100): sys.exit()

