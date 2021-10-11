import csv
from collections import Counter
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
data=Counter(height)
mode4range={
    "50-60":0,
    "60-70":0,
    "70-80":0,
}
for h,o in data.items():
    if 50<h<60:
        mode4range["50-60"]+=o
    elif 60<h<70:
        mode4range["60-70"]+=o
    elif 70<h<80:
        mode4range["70-80"]+=o
modeRange,modeO=0,0
for r,o in mode4range.items():
    if o>modeO:
        modeRange,modeO=[int(r.split("-")[0]),int(r.split("-")[1]),o]
mode=float((modeRange[0]+modeRange[1])/2)
print(mode)
    