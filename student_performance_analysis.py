import pandas as pd
import matplotlib.pyplot as plt

# Load the student performance dataset
df = pd.read_csv("student_performance.csv")

# Calculate the average score for each student
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# Display the complete dataset
print("STUDENT PERFORMANCE DATA")
print(df)

# Display average scores for each subject
print("\nAVERAGE SCORES")
print(df[["Math", "Science", "English", "Average"]].mean())

# Find the top-performing student
top_student = df.loc[df["Average"].idxmax()]

print("\nTOP PERFORMING STUDENT")
print(top_student)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(df["Student"], df["Average"])

plt.xlabel("Students")
plt.ylabel("Average Score")
plt.title("Student Performance Analysis")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
