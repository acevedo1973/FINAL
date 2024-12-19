iimport pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
file_path = "/Users/saa/Documents/BRos_110-02 SJSU/HOMEWORK ASSIGNS/FINAL PROJECT NOTES TO SEE/companies.csv"
data = pd.read_csv(file_path)

# add salary range column
data['salary_range'] = pd.cut(
    data['rating'], 
    bins=[0, 2, 3, 4, 5], 
    labels=['low', 'below average', 'average', 'high']
)

# save enhanced dataset
enhanced_file_path = "/Users/saa/Documents/BRos_110-02 SJSU/HOMEWORK ASSIGNS/FINAL PROJECT NOTES TO SEE/enhanced_companies.csv"
data.to_csv(enhanced_file_path, index=False)
print(f"enhanced dataset saved at {enhanced_file_path}")

# load enhanced dataset
data = pd.read_csv(enhanced_file_path)

# ratings distribution
plt.figure(figsize=(8, 5))
sns.histplot(data['rating'], bins=10, kde=True, color='skyblue')
plt.title("ratings distribution")
plt.xlabel("rating")
plt.ylabel("frequency")
plt.tight_layout()
plt.savefig("ratings_distribution.png")
plt.show()

# common criticisms
criticism_counts = data['critically_rated_for'].value_counts().head(10)
criticism_counts.plot(kind='bar', color='red', title='top critically rated aspects')
plt.ylabel("frequency")
plt.tight_layout()
plt.savefig("critically_rated_aspects.png")
plt.show()

# highly rated aspects
highly_rated_counts = data['highly_rated_for'].value_counts().head(10)
highly_rated_counts.plot(kind='bar', color='blue', title='top highly rated aspects')
plt.ylabel("frequency")
plt.tight_layout()
plt.savefig("highly_rated_aspects.png")
plt.show()
