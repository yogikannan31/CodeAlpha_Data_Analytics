import matplotlib.pyplot as plt

sales = [1200, 1500, 1800, 2000, 1700]
months = ["Jan", "Feb", "Mar", "Apr", "May"]

plt.plot(months, sales, marker='o')
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.show()
