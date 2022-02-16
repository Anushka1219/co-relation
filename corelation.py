import pandas as pd
import plotly.express as px
import csv
import numpy as np

coffee=[]
sleep=[]

with open("corelation.csv") as csvfile:
    df=csv.DictReader(csvfile)
    fig=px.scatter(df,x="Coffee",y="sleep",title="Co-Relation")
    print(df)
    fig.show()

    for i in df:
        coffee.append(float(i["Coffee"]))
        sleep.append(float(i["sleep"]))
    datasource={"x":coffee,"y":sleep}
c=np.corrcoef(datasource["x"],datasource["y"])
print(c)

