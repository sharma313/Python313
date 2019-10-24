'''
a=int(input())
flag=0
for x in range(1,a//2):
    if a%x==0:
        flag=1
        break
if flag==0:
    print( "is a prime")
else:
    print("is not prime")
'''
'''
a=eval(input())
for x in range(2,a+1):
    j=2
    while j<=x:
        if x%j==0:
            break
        j=j+1    
    if j==x:
       if a==j:
           print("Prime")
    
'''
def f(n):
    if n>1:
        x=n**2
        y=x+f(n-1)
        print(y)
        return f(n-1)
    else:
        return n

n=100
for x in range(0,10):
    for y in range(0,10):
        if n==x**3+y**3:
            print(x,y)
