DataY=[0,-0.9,-0.1,0.5,-2.5,-0.9,-2.1,-2.4,-0.6,2.6,3.2,2,2.4,3.5,
       3.4,3.6,0.6,3.1,3.2,1.8,3.2,3.5,2.3,6.4,4.5,5.9,6.3,9.5,5.1,4.6,7.6,9.1]
DataX=[i for i in range(len(DataY))]

W,b=0,0
LR=0.0001 #Learning Rate

Wl=[]
bl=[]

def Cost(W,b,dx,dy):
    n=len(dx)
    S=0
    for i in range(n):
        x=dx[i]
        y=dy[i]
        S+=(W*x+b-y)**2
    return S/n

def gradient_W(W,b,dx,dy):
    n=len(dx)
    S=0
    for i in range(n):
        x=dx[i]
        y=dy[i]
        S+=2*x*(x*W+b-y)
    return S/n

def gradient_b(W,b,dx,dy):
    n=len(dx)
    S=0
    for i in range(n):
        x=dx[i]
        y=dy[i]
        S+=2*(b+x*W-y)
    return S/n

def linear_regression_by_extent():
    global DataX, DataY,W,b
    extent=15

    for year in range(0,len(DataX)-extent):
        dx=DataX[year:year+extent]
        dy=DataY[year:year+extent]
        for epoch in range(100000):
            W=W-LR*(gradient_W(W,b,dx,dy))
            b=b-LR*(gradient_b(W,b,dx,dy))
        Wl.append(W)
        bl.append(b)
    print(Wl)
    print(bl)

def linear_regression_full_sweep():
    global DataX, DataY,W,b
    dx=DataX
    dy=DataY

    for epoch in range(500000):
        W=W-LR*(gradient_W(W,b,dx,dy))
        b=b-LR*(gradient_b(W,b,dx,dy))
    print(W,b)

linear_regression_by_extent()
linear_regression_full_sweep()