# -----------------------------------------------------
# HR Analytics Minor Project – Bhavya Sri Kommula
# Dataset: employe.csv (verified)
# -----------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Step 1: Load and Clean the Dataset
df = pd.read_csv('employee_data.csv')  
df.columns = df.columns.str.strip()  # Remove spaces from column names

#Step 2: Basic Exploration
print("First 5 Rows:\n", df.head())
print("\n Dataset Info:\n")
print(df.info())
print("\n Summary Statistics:\n", df.describe())
print("\n Missing Values:\n", df.isnull().sum())

# ✅ Step 3: Attrition Rate
total_employees = len(df)
employees_left = df[df['left'] == 1].shape[0]
attrition_rate = (employees_left / total_employees) * 100
print(f"\n Total Employees: {total_employees}")
print(f"❌ Employees Who Left: {employees_left}")
print(f"📉 Attrition Rate: {attrition_rate:.2f}%")

# ✅ Step 4: Department-wise Attrition
plt.figure(figsize=(8, 5))
sns.countplot(data=df[df['left'] == 1], x='dept', hue='dept', palette='Set2', legend=False)
plt.title('Employees Who Left by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees Left')
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig('department_attrition.png')
plt.show()

# ✅ Step 5: Attrition Based on Number of Projects
# Define project bins
left_few_projects = df[(df['numberOfProjects'] < 3) & (df['left'] == 1)].shape[0]
left_many_projects = df[(df['numberOfProjects'] >= 3) & (df['left'] == 1)].shape[0]

project_bins = ['< 3 Projects', '≥ 3 Projects']
left_counts = [left_few_projects, left_many_projects]
plt.figure(figsize=(6, 4))
sns.barplot(x=project_bins, y=left_counts, hue=project_bins, palette='Set1', legend=False)
plt.title("Attrition by Number of Projects")
plt.xlabel("Project Count")
plt.ylabel("Employees Who Left")
plt.tight_layout()
plt.savefig('projects_vs_attrition.png')
plt.show()



# ✅ Step 6: Salary vs Attrition (Boxplot)
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x='left', y='salary')
plt.title('Salary Distribution vs Attrition')
plt.xlabel('Attrition (0 = Stayed, 1 = Left)')
plt.ylabel('Salary Level')
plt.tight_layout()
plt.savefig('salary_vs_attrition.png')
plt.show()

# ✅ Step 7: Experience vs Project Load (Scatter Plot)
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='numberOfProjects', y='timeSpent.company', hue='left')
plt.title('Experience vs Project Load (Colored by Attrition)')
plt.xlabel('Number of Projects')
plt.ylabel('Years at Company')
plt.tight_layout()
plt.savefig('experience_vs_projects.png')
plt.show()

# ✅ Step 8: Summary File
with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(" Key Insights from HR Analytics Project:\n")
    f.write(f"- Attrition rate: {attrition_rate:.2f}%\n")
    f.write("- Highest attrition in departments: See chart.\n")
    f.write("- Employees with <3 projects are leaving more than others.\n")
    f.write("- Salary seems to impact attrition (see boxplot).\n")
    f.write("- Employees with longer time & more projects also leave.\n")
