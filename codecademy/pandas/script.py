import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.DataFrame({
    'revenue': [200, 400, 650, 800, 850],
    'cost': [150, 500, 550, 550, 560]
})

print(df1)

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time, revenue, color='green', linestyle='--', marker='s')
plt.plot(time, costs, color='grey', linestyle=':', marker='s')
plt.axis([0.5, 2, 400, 600])

plt.xlabel("Time")
plt.ylabel("Cashflows")
plt.title("Revenues and costs for a period")

plt.show()