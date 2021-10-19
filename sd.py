import math 
import pandas as pd
d=[60,61,65,63,98,99,90,95,91,96]
totalmarks=0
n=len(d)
for i in d:
    totalmarks+=i
mean=totalmarks/n
count=0
for i in d:
    x=float(i)-mean
    x=x*x
    count+=x
dev=count/n 
sd=math.sqrt(dev)
print(sd)

