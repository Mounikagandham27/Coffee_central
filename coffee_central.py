import sys 
import numpy as np

class City:
    def __init__(self,dx,dy):
        self.dx = dx
        self.dy = dy
        self.City = np.zeros(shape=(dx,dy),dtype=int)
        
    def takevalues(self,n_shops):
        return  zip(*[(map(int, values[i].split())) for i in range(1,n_shops+1)])
    
    def ans(self,x,y,q):
        xi = self.dx
        yi = self.dy
        lowerX = max(0,x-q)
        higherX = min(xi-1,x+q)
        for i in range(lowerX,higherX+1):
            rem_q = q - abs(x-i)
            lowerY = max(0,y-rem_q)
            higherY = min(yi-1,y+rem_q)
            for j in range(lowerY,higherY+1):      
                self.City[i][j] += 1

    def result(self):
        total_shops = 0
        xtemp = dx
        ytemp = 1
        for i in range(dx):
            for j in range(dy):
                if total_shops< self.City[i][j] or (total_shops == self.City[i][j] and ytemp>j) or (total_shops == self.City[i][j] and ytemp==j and xtemp<i):
                    total_shops = self.City[i][j]
                    xtemp = i+1
                    ytemp = j+1
        return total_shops,(xtemp,ytemp)

def condition(dx,dy,n_shops,queries):
    if dx != 0 or dy != 0 or n_shops != 0 or queries !=0:
       city = City(dx,dy)
       xcor, ycor = city.takevalues(n_shops)
       for l in range(1,queries+1):
           print("\nenter query",l," :")
           query = int(input())
           for i in range(0,n_shops):
               city.ans(xcor[i]-1,ycor[i]-1,query)
           print(city.result()) 
           city = City(dx,dy)
        
values = sys.stdin.readlines()
dx,dy,n_shops,queries = map(int, values[0].split())
condition(dx,dy,n_shops,queries)
