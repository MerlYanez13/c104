import csv
with open('class2.csv',newline='' )as f:
    reader=csv.reader(f)
    df=list(reader)
df.pop(0)
marks=[]
summarks=0
for i in range(len(df)):
    num=float(df[i][1])
    marks.append(num)
    summarks+=num

n=len(marks)
meanmarks=summarks/n
print(meanmarks)
import pandas as pd
import plotly.express as px
data=pd.read_csv("class2.csv")
fig=px.scatter(data,x="Student Number", y="Marks")
fig.update_layout(shapes=[dict(type='line',y0=meanmarks,y1=meanmarks, x0=0,x1=n)])
fig.show()