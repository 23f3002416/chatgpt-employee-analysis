import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Employee Performance Analysis for Healthcare Company
# Author: 23f3002416@ds.study.iitm.ac.in
# Generated with assistance from ChatGPT for TDS Data Visualization Assignment

# Generate synthetic employee performance dataset
np.random.seed(42)

# Define departments and regions
departments = ['Operations', 'Finance', 'HR', 'IT', 'Marketing', 'Sales', 'Research']
regions = ['North', 'South', 'East', 'West', 'Central']

# Generate 100 employee records
data = []
for i in range(100):
    # Weighted department selection to ensure Operations has meaningful frequency
    dept_weights = [0.25, 0.15, 0.10, 0.15, 0.10, 0.15, 0.10]  # Operations gets 25%
    department = np.random.choice(departments, p=dept_weights)
    
    region = np.random.choice(regions)
    
    # Generate performance metrics
    performance_score = np.random.normal(75, 15)  # Mean 75, std 15
    performance_score = max(0, min(100, performance_score))  # Clamp to 0-100
    
    salary = np.random.normal(65000, 20000)
    salary = max(35000, min(150000, salary))  # Realistic salary range
    
    years_experience = np.random.exponential(5)  # Exponential distribution
    years_experience = max(0, min(30, years_experience))  # 0-30 years
    
    data.append({
        'Employee_ID': f'EMP_{i+1:03d}',
        'Department': department,
        'Region': region,
        'Performance_Score': round(performance_score, 1),
        'Salary': round(salary, 0),
        'Years_Experience': round(years_experience, 1)
    })

# Create DataFrame
df = pd.DataFrame(data)

# Calculate frequency count for Operations department
operations_count = len(df[df['Department'] == 'Operations'])
print(f"Frequency count for Operations department: {operations_count}")

# Create histogram showing distribution of departments
plt.figure(figsize=(12, 8))

# Main histogram
plt.subplot(2, 1, 1)
dept_counts = df['Department'].value_counts()
colors = plt.cm.Set3(np.linspace(0, 1, len(dept_counts)))

bars = plt.bar(dept_counts.index, dept_counts.values, color=colors, alpha=0.8, edgecolor='black')
plt.title('Employee Distribution by Department\nHealthcare Company - Strategic Workforce Analysis', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Department', fontsize=12, fontweight='bold')
plt.ylabel('Number of Employees', fontsize=12, fontweight='bold')
plt.xticks(rotation=45, ha='right')

# Add value labels on bars
for bar, count in zip(bars, dept_counts.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
             str(count), ha='center', va='bottom', fontweight='bold')

# Highlight Operations department
ops_index = list(dept_counts.index).index('Operations')
bars[ops_index].set_color('#ff6b6b')
bars[ops_index].set_edgecolor('darkred')
bars[ops_index].set_linewidth(3)

plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

# Additional analysis subplot
plt.subplot(2, 1, 2)
region_dept = df.pivot_table(values='Employee_ID', index='Department', columns='Region', 
                            aggfunc='count', fill_value=0)

sns.heatmap(region_dept, annot=True, fmt='d', cmap='Blues', cbar_kws={'label': 'Employee Count'})
plt.title('Employee Distribution: Department vs Region', fontsize=14, fontweight='bold')
plt.xlabel('Region', fontsize=12, fontweight='bold')
plt.ylabel('Department', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('employee_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Print summary statistics
print("\n" + "="*60)
print("EMPLOYEE PERFORMANCE ANALYSIS SUMMARY")
print("="*60)
print(f"Contact: 23f3002416@ds.study.iitm.ac.in")
print(f"Total Employees Analyzed: {len(df)}")
print(f"Operations Department Size: {operations_count} employees ({operations_count/len(df)*100:.1f}%)")
print("\nDepartment Distribution:")
for dept, count in dept_counts.items():
    print(f"  {dept}: {count} employees")

print(f"\nKey Insights:")
print(f"- Operations is the largest department with {operations_count} employees")
print(f"- Average performance score across company: {df['Performance_Score'].mean():.1f}")
print(f"- Operations average performance: {df[df['Department']=='Operations']['Performance_Score'].mean():.1f}")
print(f"- Company-wide salary range: ${df['Salary'].min():,.0f} - ${df['Salary'].max():,.0f}")

# Save dataset for verification
df.to_csv('employee_performance_data.csv', index=False)
print(f"\nDataset saved as 'employee_performance_data.csv'")
print("Visualization saved as 'employee_analysis.png'")