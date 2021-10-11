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
meanHeight=sumHeight/n
meanWeight=sumWeight/n
print(meanHeight)
print(meanWeight)