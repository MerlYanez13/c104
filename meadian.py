import csv
with open('data.csv',newline='' )as f:
    reader=csv.reader(f)
    df=list(reader)
df.pop(0)
height=[]
weight=[]
sumHeight=0
sumWeight=0
for i in range(len(df)):
    num=float(df[i][1])
    height.append(num)
    sumHeight+=num
    num1=float(df[i][2])
    weight.append(num1)
    sumWeight+=num1

n=len(height)
height.sort()
weight.sort()
if n%2==0:
    mHeight1=height[n//2]
    mWeight1=weight[n//2]
    mHeight2=height[n//2-1]
    mWeight2=weight[n//2-1]
    medHeight=(mHeight1+mHeight2)/2
    medWeight=(mWeight1+mWeight2)/2
else:
    medHeight=height[n//2]
    medWeight=weight[n//2]
print("median",medHeight)
print("median",medWeight)
