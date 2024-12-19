import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = "/Users/saa/Documents/BRos_110-02 SJSU/HOMEWORK ASSIGNS/FINAL PROJECT NOTES TO SEE/companies.csv"
data = pd.read_csv(file_path)

# ensure salary column is numeric
data['salary_in_usd'] = pd.to_numeric(data['salary_in_usd'], errors='coerce')

# create salary ranges
data['salary_range'] = pd.cut(
    data['salary_in_usd'], 
    bins=[0, 50000, 100000, 150000, 200000, float('inf')], 
    labels=['<50k', '50k-100k', '100k-150k', '150k-200k', '200k+']
)

# create a column for it-related roles
data['is_it_role'] = data['job_title'].str.contains("IT|Tech|Developer|Engineer", case=False, na=False)

# save the modified dataset for sql and further analysis
enhanced_file_path = "/Users/saa/Documents/BRos_110-02 SJSU/HOMEWORK ASSIGNS/FINAL PROJECT NOTES TO SEE/enhanced_companies.csv"
data.to_csv(enhanced_file_path, index=False)
print(f"enhanced dataset saved at {enhanced_file_path}")

# === visualizations ===

# heatmap: average salary by region and salary range
pivot_data = data.pivot_table(
    values='salary_in_usd', 
    index='location', 
    columns='salary_range', 
    aggfunc='mean'
)
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_data, annot=True, cmap="coolwarm", fmt=".0f")
plt.title("heatmap of salary ranges by region")
plt.tight_layout()
plt.savefig("heatmap_salary_ranges.png")
plt.show()

# scatterplot: ratings vs salaries
plt.figure(figsize=(10, 6))
sns.scatterplot(x='rating', y='salary_in_usd', hue='company_size', data=data)
plt.title("scatterplot: ratings vs salaries")
plt.xlabel("ratings")
plt.ylabel("salary in usd")
plt.tight_layout()
plt.savefig("scatterplot_ratings_vs_salaries.png")
plt.show()

# print column information and salary statistics
print("\ncolumns in the dataset:")
print(data.columns)
print("\nsalary statistics:")
print(data['salary_in_usd'].describe())
