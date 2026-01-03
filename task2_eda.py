import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Marks": [78, 85, 62, 90, 74]
}

df = pd.DataFrame(data)

print(df)
print("\nMean Marks:", df["Marks"].mean())
print("Max Marks:", df["Marks"].max())
print("Min Marks:", df["Marks"].min())

plt.bar(df["Student"], df["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Analysis")
plt.show()
