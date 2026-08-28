import pandas as pd
import matplotlib.pyplot as plt

# Sample student performance dataset
data = {
    "Student": ["Alice", "Bob", "Charlie", "David", "Emma",
                "Frank", "Grace", "Henry", "Ivy", "Jack"],
    "Math": [85, 78, 92, 65, 88, 72, 95, 80, 76, 90],
    "Science": [88, 82, 90, 70, 85, 75, 94, 78, 80, 92],
    "English": [90, 75, 88, 68, 92, 78, 89, 85, 82, 94],
    "Study_Hours": [5, 4, 6, 3, 5, 4, 7, 5, 4, 6]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate average score
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

print("STUDENT PERFORMANCE DATA")
print(df)

print("\nAVERAGE SCORES")
print(df[["Math", "Science", "English", "Average"]].mean())

# Find top-performing student
top_student = df.loc[df["Average"].idxmax()]
print("\nTOP PERFORMING STUDENT")
print(top_student)

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(df["Student"], df["Average"])
plt.xlabel("Students")
plt.ylabel("Average Score")
plt.title("Student Performance Analysis")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
