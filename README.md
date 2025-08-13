# Data Visualization with ChatGPT

Employee Performance Analysis for Healthcare Company strategic workforce planning.

**Author:** 23f3002416@ds.study.iitm.ac.in

## Project Overview

This analysis demonstrates using ChatGPT to create Python-based data visualizations for employee performance analysis. The project addresses departmental distribution patterns and identifies resource allocation opportunities for executive decision-making.

## Business Context

**Organization:** Healthcare Company  
**Department:** Human Resources  
**Analysis Focus:** Employee performance across departments and regions  
**Strategic Goal:** Inform resource allocation and recruitment strategies

## Key Results

### Operations Department Analysis
- **Frequency Count:** 26 employees
- **Percentage of Workforce:** 26.0%
- **Status:** Largest department in organization
- **Performance Score:** 69.8 (vs 72.0 company average)

### Technical Implementation

#### Python Libraries Used
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
```

#### Core Analysis Code
```python
# Calculate frequency count for Operations department
operations_count = len(df[df['Department'] == 'Operations'])
print(f"Frequency count for Operations department: {operations_count}")

# Create histogram showing distribution of departments
plt.figure(figsize=(12, 8))
dept_counts = df['Department'].value_counts()
plt.bar(dept_counts.index, dept_counts.values, color=colors)
plt.title('Employee Distribution by Department')
```

#### Dataset Characteristics
- **Total Employees:** 100 records
- **Departments:** 7 (Operations, Finance, IT, Sales, Research, HR, Marketing)
- **Regions:** 5 (North, South, East, West, Central)
- **Metrics:** Performance scores, salary, experience

## Visualization Features

### Primary Histogram
- Department-wise employee distribution
- Operations department highlighted (largest at 26 employees)
- Color-coded bars for visual distinction
- Value labels on each bar
- Professional styling for executive presentation

### Secondary Analysis
- Regional distribution heatmap
- Department vs Region cross-analysis
- Performance score comparisons
- Statistical summary insights

## ChatGPT Integration

This project demonstrates ChatGPT-assisted data analysis:

1. **Dataset Generation:** Synthetic employee data creation
2. **Analysis Logic:** Statistical calculations and frequency counting
3. **Visualization Code:** Matplotlib and seaborn histogram generation
4. **Business Insights:** Strategic workforce planning recommendations

## Files Included

- `analysis.py` - Python script for data analysis and visualization
- `analysis.html` - Complete analysis report in HTML format
- `employee_analysis.png` - Generated histogram visualization
- `employee_performance_data.csv` - Synthetic dataset (100 employees)
- `README.md` - Project documentation

## Key Findings

### Department Distribution
1. **Operations:** 26 employees (26.0%) - Largest department
2. **Finance:** 19 employees (19.0%)
3. **IT:** 15 employees (15.0%)
4. **Sales:** 13 employees (13.0%)
5. **Research:** 12 employees (12.0%)
6. **HR:** 9 employees (9.0%)
7. **Marketing:** 6 employees (6.0%)

### Strategic Recommendations
- **Operations Optimization:** Address performance gap (69.8 vs 72.0 average)
- **Resource Allocation:** Leverage largest department for operational excellence
- **Recruitment Strategy:** Maintain balanced departmental distribution
- **Regional Planning:** Utilize multi-regional presence for healthcare coverage

## Validation Checklist

- ✅ Python code loads employee dataset
- ✅ Calculates Operations department frequency: **26 employees**
- ✅ Prints frequency count to console
- ✅ Creates histogram with matplotlib/seaborn
- ✅ Email verification: 23f3002416@ds.study.iitm.ac.in
- ✅ ChatGPT assistance documented
- ✅ HTML format for GitHub publication

---

*Created for TDS Data Visualization Assignment - Data Visualization with ChatGPT*REAMDE
