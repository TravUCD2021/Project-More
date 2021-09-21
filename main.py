import pandas as pd

class Assignment3:
    pass

import matplotlib.pyplot as plt

data=pd.read_csv("Assignment3.csv")

print(data)


y=data["date_time"]
x=data["amount"]
z=data["country"]


plt.bar(x,y)

plt.show()


